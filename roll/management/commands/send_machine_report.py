from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import date
from roll.models import master_final_mistake, mastermistakes
from django.conf import settings


class Command(BaseCommand):
    help = 'Send one email with all machine reports'

    def handle(self, *args, **kwargs):
        today = date.today()
        machine_ids = master_final_mistake.objects.values_list('machine_id', flat=True).distinct()

        all_machine_data = []

        for machine_id in machine_ids:
            mistakes = master_final_mistake.objects.filter(machine_id=machine_id, date=today)
            processed_mistakes = []

            for item in mistakes:
                is_bad = False
                remarks = (item.remarks or '').strip().lower()
                limits = mastermistakes.objects.filter(ty__iexact=item.types).first()

                if remarks:
                    is_bad = True

                if not is_bad and limits:
                    for i in range(1, 13):
                        value = getattr(item, f"m{i}")
                        limit = getattr(limits, f"m{i}")
                        value_clean = (value or '').strip().lower()

                        if "full roll" in value_clean:
                            is_bad = True
                            break
                        try:
                            if value and float(value) > float(limit):
                                is_bad = True
                                break
                        except (ValueError, TypeError):
                            continue

                item.status = "Bad Roll" if is_bad else "Good Roll"

                mistakes_list = []
                for i in range(1, 13):
                    val = getattr(item, f"m{i}")
                    if val and str(val).strip() not in ["", "0", "0.0"]:
                        eng_label = getattr(limits, f"mist{i}_eng", f"m{i}")
                        mistakes_list.append(f"{eng_label}-{val}")

                item.mistakes_str = "\n".join(mistakes_list).strip()
                processed_mistakes.append(item)

            total_count = len(processed_mistakes)
            good_count = sum(1 for item in processed_mistakes if item.status == "Good Roll")
            bad_count = total_count - good_count

            all_machine_data.append({
                'machine_id': machine_id,
                'mistakes': processed_mistakes,
                'total_count': total_count,
                'good_count': good_count,
                'bad_count': bad_count
            })

        # Render full email with all machines
        email_body = render_to_string('email/machine_report_email.html', {
            'machines': all_machine_data,
            'datefilter': today
        })

        subject = f"🧾 Roll checking - Daily Report ({today})"
        to_emails = ['tdhanasekaran202@gmail.com']  # Replace as needed
        from_email = settings.DEFAULT_FROM_EMAIL

        email = EmailMessage(subject, email_body, from_email, to_emails)
        email.content_subtype = "html"  # Important for sending HTML
        email.send()

        self.stdout.write(self.style.SUCCESS("✅ All machine reports emailed successfully."))
