from datetime import datetime
from roll.models import BreakTime

def break_times(request):
    now = datetime.now().time()
    bt = BreakTime.objects.filter(is_active=True).first()
    if bt:
        return {
            'break_start': bt.start_time.strftime('%H:%M:%S'),
            'break_end': bt.end_time.strftime('%H:%M:%S'),
            'in_break': bt.start_time <= now <= bt.end_time,
        }
    return {
        'break_start': '00:00:00',
        'break_end': '00:00:00',
        'in_break': False,
    }