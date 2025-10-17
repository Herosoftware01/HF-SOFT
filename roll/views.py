from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib import messages
from .models import JobAllocation,VueRl001,mastermistakes,VueOrdersinhand,master_roll_update,mistake_image,master_final_mistake,Lotsticker,Punchdtls1,VueFindia,back_permissions,BreakTime
from django.db.models import Q

import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import date
from django.db.models import F, Sum, ExpressionWrapper, IntegerField
from datetime import datetime
from django.utils.dateparse import parse_duration
from django.db.models import Min
from datetime import time
from django.core.mail import EmailMessage
from django.conf import settings


# @login_required
def home(request):
    return render(request, 'home.html')




# def custom_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('group_login_page')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})



# def custom_logout(request):
#     logout(request)
#     return redirect('login')


def group_card_selection(request):
    machines = [1,2,3,4]
    return render(request, 'group_cards.html', {'machines': machines})


# @login_required
def home(request, machine_id):
    second_user = request.session.get('second_user')
    group_id = request.session.get('group_id')

    result = None
    entered_roll = None
    latest_date = None
    today = date.today()

    emp_data = request.session.get('emp_data', {
        'emp_name_1': '',
        'emp_id1': '',
        'emp_name_2': '',
        'emp_id2': '',
    })

    job = JobAllocation.objects.filter(machine_id=machine_id, date=today).order_by('-id').first()

    if request.method == 'POST':
        if 'roll_no' in request.POST:
            entered_roll = request.POST.get('roll_no') or request.POST.get('qr')

            print(f"Searching for roll no: {entered_roll}")

          
            all_rolls = VueRl001.objects.using('demo').filter(Q(rlno__iexact=entered_roll))

            if not all_rolls.exists():
                messages.error(request, "No data found for that Roll No.")
                result = None
            else:
                # Get the latest date from the queryset
                latest_date = all_rolls.order_by('-dt').first().dt

                result = all_rolls.filter(dt=latest_date).order_by('-dt')

    return render(request, 'home.html', {
        'second_user': second_user,
        'group_id': group_id,
        'result': result,
        'searched_roll': entered_roll,
        'emp_data': emp_data,
        'job': job,
        'machine_id': machine_id,
        'latest_date': latest_date,
    })



# @login_required
from django.shortcuts import render, redirect
from datetime import date
from django.db.models import Min
from .models import JobAllocation, Punchdtls1



# def machine_jobs(request, machine_id):
#     today = date.today()

#     unique_emp_ids = Punchdtls1.objects.using('main').filter(
#         unitname='CUTTING',
#         dt=today
#     ).values('id').annotate(min_id1=Min('id1')).values_list('min_id1', flat=True)

#     employees = Punchdtls1.objects.using('main').filter(id1__in=unique_emp_ids)

#     for emp in employees:
#         raw_path = emp.id.photo if emp.id and emp.id.photo else None
#         if raw_path:
#             filename = raw_path.split('\\')[-1]
#             emp.photo_url = f"https://app.herofashion.com/staff_images/{filename}"
#         else:
#             emp.photo_url = ""

#     job = JobAllocation.objects.filter(machine_id=machine_id, date=today).order_by('-id').first()

#     if job:
#         for emp in employees:
#             if emp.id.code == job.emp_id1:
#                 job.emp_photo_1 = emp.photo_url
#             if emp.id.code == job.emp_id2:
#                 job.emp_photo_2 = emp.photo_url

#     if request.method == 'POST':
#         if 'move_user' in request.POST:
#             emp_id1 = request.POST.get('emp_id1')
#             emp_id2 = request.POST.get('emp_id2')

#             if not emp_id1 or not emp_id2:
#                 messages.error(request, "Both employee IDs are required before moving.")
#                 return redirect('machine_jobs', machine_id=machine_id)

#             request.session['emp_data'] = {
#                 'emp_name_1': request.POST.get('emp_name_1'),
#                 'emp_id1': emp_id1,
#                 'emp_name_2': request.POST.get('emp_name_2'),
#                 'emp_id2': emp_id2,
#             }
#             request.session['group_id'] = machine_id
#             return redirect('home', machine_id=machine_id)

#         else:
#             # Save allocation
#             JobAllocation.objects.create(
#                 machine_id=machine_id,
#                 date=today,
#                 emp_name_1=request.POST.get('emp_name_1', ''),
#                 emp_id1=request.POST.get('emp_id1', ''),
#                 emp_name_2=request.POST.get('emp_name_2', ''),
#                 emp_id2=request.POST.get('emp_id2', '')
#             )
#             # ✅ THIS LINE makes it trigger auto move
#             return redirect(f"{request.path}?auto_move=1")

#     return render(request, 'machine_jobs.html', {
#         'job': job,
#         'machine_id': machine_id,
#         'employees': employees
#     })



def machine_jobs(request, machine_id):
    today = date.today()

    # Get unique employee IDs for the day
    unique_emp_ids = Punchdtls1.objects.using('main').filter(
        unitname='CUTTING',
        dt=today
    ).values('id').annotate(min_id1=Min('id1')).values_list('min_id1', flat=True)

    # Fetch employee objects
    employees = Punchdtls1.objects.using('main').filter(id1__in=unique_emp_ids)

    # Add photo URL to each employee
    for emp in employees:
        raw_path = emp.id.photo if emp.id and emp.id.photo else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            emp.photo_url = f"https://app.herofashion.com/staff_images/{filename}"
        else:
            emp.photo_url = ""

    # Get the latest job allocation for this machine today
    job = JobAllocation.objects.filter(machine_id=machine_id, date=today).order_by('-id').first()

    # Attach photo to the job if exists
    if job:
        for emp in employees:
            if emp.id.code == job.emp_id1:
                job.emp_photo_1 = emp.photo_url
            if emp.id.code == job.emp_id2:
                job.emp_photo_2 = emp.photo_url

    # --- POST handling ---
    if request.method == 'POST':
        emp_id1 = request.POST.get('emp_id1', '')
        emp_name_1 = request.POST.get('emp_name_1', '')
        emp_id2 = request.POST.get('emp_id2', '')
        emp_name_2 = request.POST.get('emp_name_2', '')

        # 🔁 Move button clicked
        if 'move_user' in request.POST:
            if not emp_id1 and not emp_id2:
                messages.error(request, "At least one employee ID is required before moving.")
                return redirect('machine_jobs', machine_id=machine_id)

            request.session['emp_data'] = {
                'emp_name_1': emp_name_1,
                'emp_id1': emp_id1,
                'emp_name_2': emp_name_2,
                'emp_id2': emp_id2,
            }
            request.session['group_id'] = machine_id
            return redirect('home', machine_id=machine_id)

        # 💾 Save Allocation
        else:
            if not emp_id1 and not emp_id2:
                messages.error(request, "At least one employee must be selected.")
                return redirect('machine_jobs', machine_id=machine_id)

            # Save the job allocation
            JobAllocation.objects.create(
                machine_id=machine_id,
                date=today,
                emp_name_1=emp_name_1,
                emp_id1=emp_id1,
                emp_name_2=emp_name_2,
                emp_id2=emp_id2
            )

            # Save to session (like move_user) and redirect to home
            request.session['emp_data'] = {
                'emp_name_1': emp_name_1,
                'emp_id1': emp_id1,
                'emp_name_2': emp_name_2,
                'emp_id2': emp_id2,
            }
            request.session['group_id'] = machine_id

            return redirect('home', machine_id=machine_id)

    # --- GET request ---
    return render(request, 'machine_jobs.html', {
        'job': job,
        'machine_id': machine_id,
        'employees': employees
    })


def check_roll_exists(request):
    rollno = request.GET.get('rollno', '').strip()
    print("checking roll no", rollno)
    exists = master_roll_update.objects.filter(roll_no__iexact=rollno).exists()
    return JsonResponse({'exists': exists})

@csrf_exempt
def validate_user(request):
    if request.method != 'POST':
        return JsonResponse({'valid': False, 'error': 'Invalid method'})

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'valid': False, 'error': 'Bad JSON'})

    emp_id = data.get('emp_id')
    password = data.get('password')
    if emp_id is None or password is None:
        return JsonResponse({'valid': False, 'error': 'Missing credentials'})

    try:
        emp_id_int = int(emp_id)
    except ValueError:
        return JsonResponse({'valid': False, 'error': 'Invalid emp_id'})

    # ⚠️ Case-sensitive fix here
    user = back_permissions.objects.filter(Emp_id=emp_id_int, Password=password).first()

    if user:
        emp_name = f"{user.Emp_id}"  # Or another field like user.Name if available
        return JsonResponse({'valid': True, 'emp_name': emp_name})
    else:
        return JsonResponse({'valid': False})


# def fetch_roll_details(request):
#     roll_no = request.GET.get('rollno')
#     group_id = request.GET.get('machine_id')
#     emp_name= request.GET.get('employee_name')

#     if not roll_no:
#         messages.error(request, "No roll number provided.")
#         return redirect('home', machine_id=group_id)
    
#     # Fetch the latest matching roll entry
#     try:
#         roll_entry = VueRl001.objects.using('demo').filter(rlno__iexact=roll_no).order_by('-dt').first()
#         if not roll_entry:
#             messages.error(request, "No roll data found.")
#             return redirect('home', machine_id=group_id)
#         dc = roll_entry.dc  # Only access dc after ensuring data is not None
#         print("DC number:", dc)
#     except Exception as e:
#         messages.error(request, f"Error fetching roll data: {e}")
#         return redirect('home', machine_id=group_id)
    
#     # if master_final_mistake.objects.filter(roll_no__iexact=roll_no, dc__iexact=dc).exists():
#     #     messages.warning(request, f"Roll No {roll_no} has already been checked.")
#     #     return redirect('home', machine_id=group_id)
#     if master_final_mistake.objects.filter(roll_no__iexact=roll_no, dc_no__iexact=dc).exists():
#         messages.warning(request, f"Roll No {roll_no} with DC No {dc} has already been checked.")
#         return redirect('home', machine_id=group_id)

#     # Now get all needed fields
#     dc = roll_entry.dc
#     jobno = roll_entry.jobno
#     dia = roll_entry.dia
#     lotno = roll_entry.lotno
#     tybe = roll_entry.name
#     fabric = roll_entry.fab
#     mtr = roll_entry.mtr
#     weight = roll_entry.weight
#     color = getattr(roll_entry, 'colour', None)  # optional


#     print("jobno:", jobno)
#     print("dia:", dia)
#     print("lotno:", lotno)
#     print("tybe:", tybe)
#     print("fabric:", fabric)
#     print("mtr:", mtr)
#     print("weight:", weight)
#     print("color:", color)

#     filters = {
#         'orderno__iexact': jobno,
#         'fabric__iexact': fabric,
#         'dia__iexact': dia,
#     }
#     if color:
#         filters['colour__iexact'] = tybe

#     finaldia_queryset = VueFindia.objects.using('test').filter(**filters)
#     first_entry = finaldia_queryset.first()
#     f_dia = first_entry.finaldia if first_entry else None

#     # Debug log
#     for fin in finaldia_queryset:
#         print("orderno:", fin.orderno, "fabric:", fin.fabric, "dia:", fin.dia, "colour:", fin.colour, "finaldia:", fin.finaldia)

#     # Get image for jobno
#     image_url = VueOrdersinhand.objects.using('test').filter(orderno__iexact=jobno).values_list('img', flat=True).first()
#     full_image_url = None
#     if image_url:
#         filename = image_url.split('\\')[-1]
#         full_image_url = f"https://app.herofashion.com/order_image/{filename}"

#     # Determine mistake type list
#     if tybe and tybe.lower().startswith(('p-', 'p -')) :
#         all_mistakes = mastermistakes.objects.filter(ty__istartswith='p')
#         types = "p"
#     else:
#         all_mistakes = mastermistakes.objects.filter(ty__iexact='d')
#         types = "d"

#     return render(request, "mistakes.html", {
#         'roll_no': roll_no,
#         'group_id': group_id,
#         'dc': dc,
#         'types': types,
#         'mtr': mtr,
#         'emp_name': emp_name,
#         'lotno': lotno,
#         'weight': weight,
#         'fabric': fabric,
#         'jobno': jobno,
#         'tybe': tybe,
#         'f_dia': f_dia,
#         'color': color,
#         'image_url': image_url,
#         'full_image_url': full_image_url,
#         'all_mistakes': all_mistakes
#     })




def fetch_roll_details(request):
    roll_no = request.GET.get('rollno')
    group_id = request.GET.get('machine_id')
    emp_name = request.GET.get('employee_name')

    if master_roll_update.objects.filter(roll_no__iexact=roll_no).exists():
        if not emp_name:
            # No emp_name passed → they didn't do login flow
            messages.error(request, "This roll no already exists. Please scan and enter employee credentials.")
            # Redirect back or to a page where user can try again
            return redirect('home/{group_id}/')

    now = datetime.now().time()
    bt = BreakTime.objects.filter(is_active=True).first()

    # ✅ Break active check: redirect to break screen and save original URL
    if bt and bt.start_time <= now <= bt.end_time:
        if not request.path.startswith('/roll/break/'):
            if 'original_url' not in request.session:
                # ✅ Save current full path with GET params
                request.session['original_url'] = request.get_full_path()
                print("Saving original_url:", request.get_full_path())  # Optional for debug
            return redirect('/roll/break/')
        

    def safe_redirect_home():
        """Redirect safely to home or fallback."""
        if group_id:
            return redirect('home', machine_id=group_id)
        else:
            messages.error(request, "Machine ID is missing for redirect.")
            return redirect('/roll/')  # 🔁 Replace with a safe default view name

    # Step 1: Validate roll number
    if not roll_no:
        messages.error(request, "No roll number provided.")
        return safe_redirect_home()

    # Step 2: Fetch roll entry
    try:
        roll_entry = VueRl001.objects.using('demo').filter(rlno__iexact=roll_no).order_by('-dt').first()
        if not roll_entry:
            messages.error(request, "No roll data found.")
            return safe_redirect_home()

        dc = roll_entry.dc  # Access safely after ensuring roll_entry is not None
        print("DC number:", dc)
    except Exception as e:
        messages.error(request, f"Error fetching roll data: {e}")
        return safe_redirect_home()

    # Step 3: Check for duplicate entry
    if master_final_mistake.objects.filter(roll_no__iexact=roll_no, dc_no__iexact=dc).exists():
        messages.warning(request, f"Roll No {roll_no} with DC No {dc} has already been checked.")
        return safe_redirect_home()

    # Step 4: Extract roll details
    jobno = roll_entry.jobno
    dia = roll_entry.dia
    lotno = roll_entry.lotno
    tybe = roll_entry.name
    fabric = roll_entry.fab
    mtr = roll_entry.mtr
    weight = roll_entry.weight
    color = getattr(roll_entry, 'colour', None)

    print("jobno:", jobno)
    print("dia:", dia)
    print("lotno:", lotno)
    print("tybe:", tybe)
    print("fabric:", fabric)
    print("mtr:", mtr)
    print("weight:", weight)
    print("color:", color)

    # Step 5: Fetch finaldia if available
    filters = {
        'orderno__iexact': jobno,
        'fabric__iexact': fabric,
        'dia__iexact': dia,
    }
    if color:
        filters['colour__iexact'] = tybe

    finaldia_queryset = VueFindia.objects.using('test').filter(**filters)
    first_entry = finaldia_queryset.first()
    f_dia = first_entry.finaldia if first_entry else None

    # Debug log for all matched entries
    for fin in finaldia_queryset:
        print("orderno:", fin.orderno, "fabric:", fin.fabric, "dia:", fin.dia, "colour:", fin.colour, "finaldia:", fin.finaldia)

    # Step 6: Get job image
    image_url = VueOrdersinhand.objects.using('test').filter(orderno__iexact=jobno).values_list('img', flat=True).first()
    full_image_url = None
    if image_url:
        filename = image_url.split('\\')[-1]
        full_image_url = f"https://app.herofashion.com/order_image/{filename}"

    # Step 7: Determine mistake type list
    if tybe and tybe.lower().startswith(('p-', 'p -')):
        all_mistakes = mastermistakes.objects.filter(ty__istartswith='p')
        types = "p"
    else:
        all_mistakes = mastermistakes.objects.filter(ty__iexact='d')
        types = "d"

    # Step 8: Render the response
    return render(request, "mistakes.html", {
        'roll_no': roll_no,
        'group_id': group_id,
        'dc': dc,
        'types': types,
        'mtr': mtr,
        'emp_name': emp_name,
        'lotno': lotno,
        'weight': weight,
        'fabric': fabric,
        'jobno': jobno,
        'tybe': tybe,
        'f_dia': f_dia,
        'color': color,
        'image_url': image_url,
        'full_image_url': full_image_url,
        'all_mistakes': all_mistakes
    })


# @csrf_exempt
# def save_roll_update(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             roll_no = data.get('roll_no')
#             # field = data.get('field')
#             field = data.get('field') 
#             value = data.get('value')

#             print(f"Received data: roll_no={roll_no}, field={field}, value={value}")

#             if not (roll_no and field and value is not None):
#                 return JsonResponse({'error': 'Missing data'}, status=400)

#             # Normalize roll_no to lowercase to avoid duplicates
#             roll_no = roll_no.strip().lower()

#             # Try to find existing record (case-insensitive)
#             record = master_roll_update.objects.filter(roll_no__iexact=roll_no).first()

#             if not record:
#                 record = master_roll_update.objects.create(
#                     roll_no=roll_no,
#                     dc_no='',
#                     lot_no='',
#                     field_id='',
#                     types=''
#                 )

#             if field == 'timer':
#                 try:
#                     parsed_time = datetime.strptime(value, '%H:%M:%S').time()
#                     record.timer = parsed_time
#                 except ValueError:
#                     return JsonResponse({'error': 'Invalid time format'}, status=400)
#             else:
#                 # Generic field update
#                 if hasattr(record, field):
#                     setattr(record, field, value)
#                 else:
#                     return JsonResponse({'error': f"Field '{field}' does not exist"}, status=400)

#             record.save()
#             print("Saved successfully")
#             print(f"Updating {roll_no} - setting {field} = {value}")
#             return JsonResponse({'status': 'success', 'field': field, 'value': value})

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=405)



@csrf_exempt
def save_roll_update(request):
    if request.method == 'POST':
        try:
            # Load JSON data from request
            data = json.loads(request.body)

            roll_no = data.get('roll_no')
            field = data.get('field')
            value = data.get('value')

            print(f"📥 Received data: roll_no={roll_no}, field={field}, value={value}")

            if not (roll_no and field and value is not None):
                return JsonResponse({'error': 'Missing data'}, status=400)

            # Normalize roll_no to lowercase
            roll_no = roll_no.strip().lower()

            # 🔍 Get record from correct DB (use 'default' unless you need a specific DB)
            record = master_roll_update.objects.filter(roll_no__iexact=roll_no).first()

            if not record:
                record = master_roll_update.objects.create(
                    roll_no=roll_no,
                    dc_no='',
                    lot_no='',
                    field_id='',
                    types=''
                )
                print("🆕 Created new record")

            print(f"🆔 Record PK: {record.pk}")

            # 🕒 Handle timer field separately
            if field == 'timer':
                try:
                    parsed_time = datetime.strptime(value, '%H:%M:%S').time()
                    record.timer = parsed_time
                    record.save()
                    print(f"⏱️ Timer set to: {record.timer}")
                except ValueError:
                    return JsonResponse({'error': 'Invalid time format'}, status=400)
            else:
               
                if hasattr(record, field):
                    setattr(record, field, value)

                    # Debug before saving
                    print(f"✅ Before save: {field} = {getattr(record, field)}")

                    record.save()

                    # Debug after saving
                    print(f"✅ After save: {field} = {getattr(record, field)}")
                else:
                    return JsonResponse({'error': f"Field '{field}' does not exist"}, status=400)

            return JsonResponse({
                'status': 'success',
                'field': field,
                'value': value
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)




# def fetch_roll_data(request, roll_no):
#     print(f"🎯 Fetching roll data for roll_no: {roll_no}")

#     obj = master_roll_update.objects.filter(roll_no__iexact=roll_no).first()

#     if obj:
#         data = {f"m{i}": getattr(obj, f"m{i}") for i in range(1, 13)}
#         data["timer"] = obj.timer.strftime("%H:%M:%S") if obj.timer else "00:00:00"
#         return JsonResponse({"success": True, "data": data})
#     else:
#         print("❌ Roll number not found in master_roll_update table.")
#         data = {f"m{i}": "" for i in range(1, 13)}
#         data["timer"] = "00:00:00"
#         return JsonResponse({"success": True, "data": data})

def fetch_roll_data(request, roll_no):
    print(f"🎯 Fetching roll data for roll_no: {roll_no}")

    # Step 1: Get roll entry from VueRl001 (demo DB)
    roll_entry = VueRl001.objects.using('demo').filter(rlno__iexact=roll_no).order_by('-dt').first()

    if not roll_entry:
        print("❌ No matching roll found in VueRl001.")
        data = {f"m{i}": "" for i in range(1, 13)}
        data["timer"] = "00:00:00"
        return JsonResponse({"success": False, "message": "Roll not found in source DB.", "data": data})

    dc = roll_entry.dc.strip() if roll_entry.dc else ""
    print(f"✅ Found roll in VueRl001. Using DC No: {dc}")

    # Step 2: Try to fetch matching master_roll_update object
    obj = master_roll_update.objects.filter(
        roll_no__iexact=roll_no,
        dc_no__iexact=dc
    ).first()

    if obj:
        print("✅ Found existing record in master_roll_update.")
        data = {f"m{i}": getattr(obj, f"m{i}") for i in range(1, 13)}
        data["timer"] = obj.timer.strftime("%H:%M:%S") if obj.timer else "00:00:00"
        return JsonResponse({"success": True, "data": data})

    # Step 3: Record not found — create new one with default values
    print("🆕 Creating new record in master_roll_update.")

    obj = master_roll_update.objects.create(
        roll_no=roll_no,
        dc_no=dc,
        timer=time(0, 0, 0),  # 00:00:00
        **{f"m{i}": "" for i in range(1, 13)}
    )

    data = {f"m{i}": "" for i in range(1, 13)}
    data["timer"] = "00:00:00"
    return JsonResponse({"success": True, "data": data})


def manifest(request):
    data = {
        "name": "roll",
        "short_name": "roll",
        "description": "My Django PWA Application",
        "start_url": "/",
        "display": "standalone",
        "scope": "/",
        "orientation": "portrait",
        "background_color": "#ffffff",
        "theme_color": "#000000",
        "status_bar": "default",
        "icons": [
            {"src": "/static/images/image.png", "sizes": "192x192"},
            {"src": "/static/images/image.png", "sizes": "512x512"}
        ],
        "dir": "auto",
        "lang": "en-US",
        "screenshots": [],
        "shortcuts": []
    }
    return JsonResponse(data)



from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import mastermistakes

def submit_mistake(request):
    all = mastermistakes.objects.all()

    # Check if editing
    edit_id = request.GET.get('edit')
    edit_instance = None
    if edit_id:
        edit_instance = get_object_or_404(mastermistakes, id=edit_id)

    # Handle Delete
    if request.method == 'POST' and 'delete_id' in request.POST:
        delete_id = request.POST.get('delete_id')
        to_delete = get_object_or_404(mastermistakes, id=delete_id)
        to_delete.delete()
        return redirect('submit_mistake')

    # Handle Create or Update
    if request.method == 'POST' and 'delete_id' not in request.POST:
        data = edit_instance if edit_instance else mastermistakes()
        data.ty = request.POST.get('ty')
        data.dt = timezone.now()
        data.mist1_eng = request.POST.get('mist1_eng')
        data.mist2_eng = request.POST.get('mist2_eng')
        data.mist3_eng = request.POST.get('mist3_eng')
        data.mist4_eng = request.POST.get('mist4_eng')
        data.mist5_eng = request.POST.get('mist5_eng')
        data.mist6_eng = request.POST.get('mist6_eng')
        data.mist7_eng = request.POST.get('mist7_eng')
        data.mist8_eng = request.POST.get('mist8_eng')
        data.mist9_eng = request.POST.get('mist9_eng')
        data.mist10_eng = request.POST.get('mist10_eng')
        data.mist11_eng = request.POST.get('mist11_eng')
        data.mist12_eng = request.POST.get('mist12_eng')
        data.mist1_ta = request.POST.get('mist1_ta')
        data.mist2_ta = request.POST.get('mist2_ta')
        data.mist3_ta = request.POST.get('mist3_ta')
        data.mist4_ta = request.POST.get('mist4_ta')
        data.mist5_ta = request.POST.get('mist5_ta')
        data.mist6_ta = request.POST.get('mist6_ta')
        data.mist7_ta = request.POST.get('mist7_ta')
        data.mist8_ta = request.POST.get('mist8_ta')
        data.mist9_ta = request.POST.get('mist9_ta')
        data.mist10_ta = request.POST.get('mist10_ta')
        data.mist11_ta = request.POST.get('mist11_ta')
        data.mist12_ta = request.POST.get('mist12_ta')
        data.mist1_hin = request.POST.get('mist1_hin')
        data.mist2_hin = request.POST.get('mist2_hin')
        data.mist3_hin = request.POST.get('mist3_hin')
        data.mist4_hin = request.POST.get('mist4_hin')
        data.mist5_hin = request.POST.get('mist5_hin')
        data.mist6_hin = request.POST.get('mist6_hin')
        data.mist7_hin = request.POST.get('mist7_hin')
        data.mist8_hin = request.POST.get('mist8_hin')
        data.mist9_hin = request.POST.get('mist9_hin')
        data.mist10_hin = request.POST.get('mist10_hin')
        data.mist11_hin = request.POST.get('mist11_hin')
        data.mist12_hin = request.POST.get('mist12_hin')
        data.m1_choice = request.POST.get('m1_choice')
        data.m2_choice = request.POST.get('m2_choice')
        data.m3_choice = request.POST.get('m3_choice')
        data.m4_choice = request.POST.get('m4_choice')
        data.m5_choice = request.POST.get('m5_choice')
        data.m6_choice = request.POST.get('m6_choice')
        data.m7_choice = request.POST.get('m7_choice')
        data.m8_choice = request.POST.get('m8_choice')
        data.m9_choice = request.POST.get('m9_choice')
        data.m10_choice = request.POST.get('m10_choice')
        data.m11_choice = request.POST.get('m11_choice')
        data.m12_choice = request.POST.get('m12_choice')
        data.m1 = request.POST.get('m1') or 0
        data.m2 = request.POST.get('m2') or 0
        data.m3 = request.POST.get('m3') or 0
        data.m4 = request.POST.get('m4') or 0
        data.m5 = request.POST.get('m5') or 0
        data.m6 = request.POST.get('m6') or 0
        data.m7 = request.POST.get('m7') or 0
        data.m8 = request.POST.get('m8') or 0
        data.m9 = request.POST.get('m9') or 0
        data.m10 = request.POST.get('m10') or 0
        data.m11 = request.POST.get('m11') or 0
        data.m12 = request.POST.get('m12') or 0

        # Image uploads (only update if provided)
        for i in range(1, 13):
            file_field = f'mist{i}_img'
            file_value = request.FILES.get(file_field)
            if file_value:
                setattr(data, file_field, file_value)

        data.save()
        return redirect('submit_mistake')

    return render(request, 'mistake_form.html', {
        'all': all,
        'edit_instance': edit_instance
    })



def upload_images(request):
    if request.method == 'POST':
        lot_no = request.POST.get('lot_no')
        job_no = request.POST.get('job_no')
        roll_no = request.POST.get('roll_no')
        machine_id = request.POST.get('machine_id')
        color = request.POST.get('color')

        uploaded_urls = []

        for file in request.FILES.getlist('images'):
            img = mistake_image.objects.create(
                lot_no=lot_no,
                job_no=job_no,
                roll_no=roll_no,
                machine_id=machine_id,
                color=color,
                image=file
            )
            uploaded_urls.append(img.image.url)

        return JsonResponse({'status': 'success', 'images': uploaded_urls})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def view_images(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        job_no = request.GET.get('job_no')
        roll_no = request.GET.get('roll_no')
        color = request.GET.get('color')

        images = mistake_image.objects.filter(
            job_no=job_no,
            roll_no=roll_no,
            color=color
        )

        image_urls = [img.image.url for img in images]
        return JsonResponse({'images': image_urls})

    return render(request, 'mistakes.html')


import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def save_final_data(request):
    # data = mastermistakes.objects.all()
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Data received:", data)

            timer_str = data.get('timer', '').strip()
            timer_obj = None
            if timer_str:
                try:
                    timer_obj = datetime.strptime(timer_str, '%H:%M:%S').time()
                except ValueError:
                    timer_obj = None  # Could log or handle bad format here

            roll_no=data.get('roll_no', '')
            roll_entry = VueRl001.objects.using('demo').filter(rlno__iexact=roll_no).order_by('-dt').first()
            color =roll_entry.name

            instance = master_final_mistake.objects.create(
                roll_no=data.get('roll_no', ''),
                job_no=data.get('job_no', ''),
                machine_id=data.get('machine_id', ''),
                dc_no=data.get('dc_no', ''),
                lot_no=data.get('lot_no', ''),
                color=color,
                # field_id=data.get('field_id', ''),
                types=data.get('types', ''), # Set if needed
                timer=timer_obj,
                m1=data.get('m1', ''),
                m2=data.get('m2', ''),
                m3=data.get('m3', ''),
                m4=data.get('m4', ''),
                m5=data.get('m5', ''),
                m6=data.get('m6', ''),
                m7=data.get('m7', ''),
                m8=data.get('m8', ''),
                m9=data.get('m9', ''),
                m10=data.get('m10', ''),
                m11=data.get('m11', ''),
                m12=data.get('m12', ''),
                finish_dia=data.get('finish_dia', ''),
                total_meters=data.get('total_meters', ''),
                act_gsm=data.get('act_gsm', ''),
                remarks=data.get('remarks', '')
            )

            try:
                u_value = float(data.get('meter', 0))
            except (ValueError, TypeError):
                u_value = 0.0

            u_data = "kgs" if u_value == 0.0 else "meters"
            
            emp_name = data.get('emp_name', '')
            gsm = data.get('act_gsm')
            gsm_cleaned = int(gsm) if gsm and gsm.isdigit() else 0

            m1_value = data.get('m1', '').strip()
            m2_value = data.get('m2', '').strip()
            m3_value = data.get('m3', '').strip()
            m4_value = data.get('m4', '').strip()
            m5_value = data.get('m5', '').strip()
            m6_value = data.get('m6', '').strip()
            m7_value = data.get('m7', '').strip()
            m8_value = data.get('m8', '').strip()
            m9_value = data.get('m9', '').strip()
            m10_value = data.get('m10', '').strip()
            m11_value = data.get('m11', '').strip()
            m12_value = data.get('m12', '').strip()
            ty = data.get('types', '')

            print("type:", ty)
            matched_mistake = mastermistakes.objects.filter(ty__iexact=ty).first()

            if matched_mistake:
                mistakes = []

                if m1_value:
                    mistakes.append(f"{matched_mistake.mist1_eng} - {m1_value}")
                if m2_value:
                    mistakes.append(f"{matched_mistake.mist2_eng} - {m2_value}")
                if m3_value:
                    mistakes.append(f"{matched_mistake.mist3_eng} - {m3_value}")
                if m4_value:
                    mistakes.append(f"{matched_mistake.mist4_eng} - {m4_value}")
                if m5_value:
                    mistakes.append(f"{matched_mistake.mist5_eng} - {m5_value}")
                if m6_value:
                    mistakes.append(f"{matched_mistake.mist6_eng} - {m6_value}")
                if m7_value:
                    mistakes.append(f"{matched_mistake.mist7_eng} - {m7_value}")
                if m8_value:
                    mistakes.append(f"{matched_mistake.mist8_eng} - {m8_value}")
                if m9_value:
                    mistakes.append(f"{matched_mistake.mist9_eng} - {m9_value}")
                if m10_value:
                    mistakes.append(f"{matched_mistake.mist10_eng} - {m10_value}")
                if m11_value:
                    mistakes.append(f"{matched_mistake.mist11_eng} - {m11_value}")
                if m12_value:
                    mistakes.append(f"{matched_mistake.mist12_eng} - {m12_value}")

                combined_m1 = "\n".join(mistakes)  # newline-separated
            else:
                combined_m1 = m1_value  # fallback to just m1 if type not found
                            

            print("Combined M1:", combined_m1)

            # Lotsticker.objects.using('demo').all().delete()
            # lotsticker_instance = Lotsticker.objects.using('demo').create(
            #     lotno=data.get('lot_no', ''),
            #     colour=data.get('color', ''),
            #     rollno=data.get('roll_no', ''),
            #     dcno=data.get('dc_no', ''),
            #     fabric=data.get('fabric', ''),
            #     wgt=data.get('weight', 0),
            #     m1=combined_m1,
 
            #     # fdia=data.get('finish_dia', ''),
            #     mtr=data.get('total_meters', 0),
            #     jobno=data.get('job_no', ''),
            #     dia=data.get('finish_dia', ''),
            #     gsm=gsm_cleaned,
            #     re=data.get('remarks', ''),
            #     em=emp_name,
            #     u=u_data,
            # )

            matched_image = mistake_image.objects.filter(
                roll_no=data.get('roll_no', ''),
                lot_no=data.get('lot_no', ''),
                job_no=data.get('job_no', '')
            ).first()

            if matched_image and matched_image.image:
                subject = "Mistake Alert - Roll Issue Detected"
                body = f"""
                A matching mistake entry has been recorded.

                📦 Roll No: {matched_image.roll_no}
                📦 Lot No: {matched_image.lot_no}
                📦 Job No: {matched_image.job_no}
                🎨 Color: {matched_image.color}
                """

                email = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=['tdhanasekaran202@gmail.com'],  # Replace with your recipient list
                )

                # Attach the image
                if matched_image.image:
                    image_path = matched_image.image.path  # Full path to the image
                    email.attach_file(image_path)

                try:
                    email.send(fail_silently=False)
                    print("✅ Email with image sent.")
                except Exception as email_error:
                    print("❌ Failed to send email:", email_error)

            return JsonResponse({
                'status': 'success',
                'id': instance.id,
                # 'lotsticker_id': lotsticker_instance.sl,
                'machine_id': data.get('machine_id', '')
            })
            
            # return JsonResponse({'status': 'success', 'id': instance.id, 'machine_id': data.get('machine_id', '')})

        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
            # Optional: log the error e
            # return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'invalid'}, status=400)


def roll_report(request):
    update = master_roll_update.objects.all()
    final =master_final_mistake.objects.all()
    return render(request, 'roll_report.html',{'update':update,'final':final})


def delete_roll(request):
    if request.method == "POST":
        roll_no = request.POST.get("roll_no")

        master_final_mistake.objects.filter(roll_no__iexact=roll_no).delete()
        master_roll_update.objects.filter(roll_no__iexact=roll_no).delete()

    return redirect('roll_report')



# def machine_report(request, machine_id):
#     roll_no = request.GET.get('rollfilter', '').strip()
#     datefilter = request.GET.get('datefilter')
#     roll_status = request.GET.get('roll_status', 'all')  # 'all', 'good_roll', 'bad_roll'

#     print("roll_status==",roll_status)
#     machine_id = machine_id

#     mistakes = master_final_mistake.objects.filter(machine_id=machine_id)

#     if roll_no:
#         mistakes = mistakes.filter(roll_no__icontains=roll_no)

#     if datefilter:
#         mistakes = mistakes.filter(date=datefilter)
#     elif not roll_no:
#         mistakes = mistakes.filter(date=date.today())

#     # default_limits = mastermistakes.objects.first()
    

#     processed_mistakes = []
#     for item in mistakes:
#         is_bad = False
#         remarks = (item.remarks or '').strip().lower()
#         print("item_types:", item.types)
#         limits = mastermistakes.objects.filter(ty__iexact=item.types).first() 

#         if remarks:
#             is_bad = True

#         if not is_bad and limits:
#             for i in range(1, 13):
#                 value = getattr(item, f"m{i}")
#                 limit = getattr(limits, f"m{i}")
#                 value_clean = (value or '').strip().lower()

#                 if "full roll" in value_clean:
#                     is_bad = True
#                     break

#                 try:
#                     if value and float(value) > float(limit):
#                         is_bad = True
#                         break
#                 except (ValueError, TypeError):
#                     continue  

#         # item.status = "Bad Roll" if is_bad else "Good Roll"
#         item.status = "Fail Roll" if is_bad else "Pass Roll"

#         mistakes_list = []
#         for i in range(1, 13):
#             val = getattr(item, f"m{i}")
#             if val and str(val).strip() not in ["", "0", "0.0"]:
#                 eng_label = getattr(limits, f"mist{i}_eng", f"m{i}")
#                 mistakes_list.append(f"{eng_label}-{val}")
        
#         item.mistakes_str = "\n".join(mistakes_list).strip()

#         processed_mistakes.append(item)

#     total_count = len(processed_mistakes)
#     good_count = sum(1 for item in processed_mistakes if item.status == "Good Roll")
#     bad_count = total_count - good_count

#     if roll_status == "good_roll":
#         processed_mistakes = [item for item in processed_mistakes if item.status == "Pass Roll"]
#     elif roll_status == "bad_roll":
#         processed_mistakes = [item for item in processed_mistakes if item.status == "Fail Roll"]

#     return render(request, 'machine_report.html', {
#         'mistakes': processed_mistakes,
#         'rollfilter': roll_no,
#         'datefilter': datefilter or '',
#         'total_count': total_count,
#         'good_count': good_count,
#         'bad_count': bad_count,
#         'roll_status': roll_status,
#         'machine_id': machine_id
#     })


def machine_report(request, machine_id):
    roll_no = request.GET.get('rollfilter', '').strip()
    datefilter = request.GET.get('datefilter')
    roll_status = request.GET.get('roll_status', 'all')  # 'all', 'good_roll', 'bad_roll'

    mistakes = master_final_mistake.objects.filter(machine_id=machine_id)

    for data in mistakes:
        print("timer == ", data.timer)
    

    if roll_no:
        mistakes = mistakes.filter(
            Q(roll_no__icontains=roll_no) |
            Q(lot_no__icontains=roll_no) |
            Q(job_no__icontains=roll_no) |
            Q(color__icontains=roll_no)
        )

    if datefilter:
        mistakes = mistakes.filter(date=datefilter)
    elif not roll_no:
        mistakes = mistakes.filter(date=date.today())

    processed_mistakes = []
    for item in mistakes:
        item.timer_str = str(item.timer)
        try:
            item.timer_seconds = item.timer.hour * 3600 + item.timer.minute * 60 + item.timer.second
            item.is_timer_exceeded = item.timer_seconds > 300  # 5 minutes = 300 seconds
        except:
            item.is_timer_exceeded = False

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

        item.status = "Fail Roll" if is_bad else "Pass Roll"

        mistakes_list = []
        for i in range(1, 13):
            val = getattr(item, f"m{i}")
            if val and str(val).strip() not in ["", "0", "0.0"]:
                eng_label = getattr(limits, f"mist{i}_eng", f"m{i}")
                mistakes_list.append(f"{eng_label}-{val}")

        item.mistakes_str = "\n".join(mistakes_list).strip()
        processed_mistakes.append(item)

    total_count = len(processed_mistakes)
    good_count = sum(1 for item in processed_mistakes if item.status == "Pass Roll")
    bad_count = total_count - good_count

    if roll_status == "good_roll":
        processed_mistakes = [item for item in processed_mistakes if item.status == "Pass Roll"]
    elif roll_status == "bad_roll":
        processed_mistakes = [item for item in processed_mistakes if item.status == "Fail Roll"]

    return render(request, 'machine_report.html', {
        'mistakes': processed_mistakes,
        'rollfilter': roll_no,
        'datefilter': datefilter or '',
        'total_count': total_count,
        'good_count': good_count,
        'bad_count': bad_count,
        'roll_status': roll_status,
        'machine_id': machine_id
    })



# def break_screen(request):
#     now = datetime.now().time()
#     breaks = BreakTime.objects.filter(is_active=True)

#     # ✅ Store the original URL if passed
#     original_url = request.GET.get('original_url')
#     if original_url:
#         request.session['original_url'] = original_url

#     for bt in breaks:
#         if bt.start_time <= now <= bt.end_time:
#             return render(request, 'break.html', {
#                 'break_end_time': bt.end_time.strftime('%H:%M:%S')
#             })

#     # ✅ Break is over → redirect to original or fallback
#     original = request.session.pop('original_url', None)
#     if original:
#         return redirect(original)
#     return redirect('/roll/')  # fallback


# # ✅ New: API to check break status in real-time via JS
# def get_current_break(request):
#     now = datetime.now().time()
#     breaks = BreakTime.objects.filter(is_active=True)

#     for bt in breaks:
#         if bt.start_time <= now <= bt.end_time:
#             return JsonResponse({
#                 'in_break': True,
#                 'start_time': bt.start_time.strftime('%H:%M:%S'),
#                 'end_time': bt.end_time.strftime('%H:%M:%S')
#             })

#     return JsonResponse({
#         'in_break': False
#     })


def break_times(request):
    now = datetime.now().time()
    breaks = BreakTime.objects.filter(is_active=True)

    for bt in breaks:
        if bt.start_time <= now <= bt.end_time:
            return {
                'break_start': bt.start_time.strftime('%H:%M:%S'),
                'break_end': bt.end_time.strftime('%H:%M:%S'),
                'in_break': True,
            }

    return {
        'break_start': '00:00:00',
        'break_end': '00:00:00',
        'in_break': False,
    }


def break_screen(request):
    now = datetime.now()
    breaks = BreakTime.objects.filter(is_active=True)

    original_url = request.GET.get('original_url')
    # Only set original_url in session if not already set
    if original_url and not request.session.get('original_url'):
        request.session['original_url'] = original_url

    for bt in breaks:
        if bt.start_time <= now.time() <= bt.end_time:
            break_end_dt = datetime.combine(now.date(), bt.end_time)
            return render(request, 'break.html', {
                'break_end_ts': int(break_end_dt.timestamp() * 1000),  # JS timestamp in ms
                'server_now_ts': int(now.timestamp() * 1000),          # server current time ms
            })

    # Break is over, redirect to original URL or fallback
    original = request.session.pop('original_url', None)
    if original:
        return redirect(original)
    return redirect('/roll/')


def get_current_break(request):
    now = datetime.now().time()
    breaks = BreakTime.objects.filter(is_active=True)

    for bt in breaks:
        if bt.start_time <= now <= bt.end_time:
            return JsonResponse({
                'in_break': True,
                'start_time': bt.start_time.strftime('%H:%M:%S'),
                'end_time': bt.end_time.strftime('%H:%M:%S')
            })

    return JsonResponse({'in_break': False})