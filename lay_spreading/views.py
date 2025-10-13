from django.shortcuts import render,redirect, get_object_or_404
from .models import layemployee,Empwisesal,Punchdtls1,VuePlandtlsTablewise,VuePlandetails,overwrite_permissions,table_lock,lay_data_update,TrsCplan4,roll_data_update,final_plans
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.db.models import Min
from datetime import time,date
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


def home(request):
    return render(request, "lay/home.html")


def emp(request, id):
    today = date.today()

    record = (
        layemployee.objects
        .filter(table__exact=id, date=today)
        .order_by('-id')  
        .first()
    )

    # Fallback values
    if record:
        initial = [
            record.emp1 or "",
            record.emp2 or "",
            record.emp3 or "",
            record.emp4 or "",
            record.emp5 or "",
            record.emp6 or "",
        ]
    else:
        initial = ["", "", "", "", "", ""]

    return render(request, "lay/emp.html", {
        'id': id,
        'initial_emps': initial,
    })

# def task(request, id):
  
#     # cutsample = VuePlandtlsTablewise.objects.using('demo').filter(tableno__exact=id,sample_descr__iexact='CUTTING SAMPLE').order_by('-rownum')
#     cutsample_count = VuePlandtlsTablewise.objects.using('demo').filter(tableno__exact=id,sample_descr__iexact='CUTTING SAMPLE').count()
#     orders = VuePlandtlsTablewise.objects.using('demo').filter(tableno__exact=id,sample_descr__iexact='ORDER').order_by('-rownum')
#     order_count = VuePlandtlsTablewise.objects.using('demo').filter(tableno__exact=id,sample_descr__iexact='ORDER').count()
#     lock_status = table_lock.objects.first()
#     return render(request, "lay/task.html", {'id': id, 'datas': cutsample,'orders':orders,'cutsample_count':cutsample_count,'order_count':order_count,'lock_status':lock_status})



from lay_spreading.models import final_plans, VuePlandtlsTablewise

def task(request, id):
    # Step 1: Get plan_nos from SQLite
    existing_plan_nos = list(final_plans.objects.values_list('plan_no', flat=True))
    print("Existing plan_nos:", existing_plan_nos)

    # Step 2: Use that list in the MSSQL query (with .using('demo'))
    cutsample = VuePlandtlsTablewise.objects.using('demo') \
        .filter(tableno=id, sample_descr__iexact='CUTTING SAMPLE') \
        .exclude(planno__in=existing_plan_nos) \
        .order_by('-rownum')

    # Continue as normal
    cutsample_count = cutsample.count()
    orders = VuePlandtlsTablewise.objects.using('demo') \
        .filter(tableno=id, sample_descr__iexact='ORDER') \
        .exclude(planno__in=existing_plan_nos) \
        .order_by('-rownum')
    order_count = orders.count()
    lock_status = table_lock.objects.first()

    return render(request, "lay/task.html", {
        'id': id,
        'datas': cutsample,
        'orders': orders,
        'cutsample_count': cutsample_count,
        'order_count': order_count,
        'lock_status': lock_status
    })


@csrf_exempt
def save_emp_ids(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            emp_ids = data.get('emp_ids', [])
            table_id = data.get('table')  # get table ID from frontend

            # Pad emp_ids to always have 6 items
            emp_ids += [""] * (6 - len(emp_ids))

            layemployee.objects.create(
                emp1=emp_ids[0],
                emp2=emp_ids[1],
                emp3=emp_ids[2],
                emp4=emp_ids[3],
                emp5=emp_ids[4],
                emp6=emp_ids[5],
                table=table_id
            )
            
            request.session['emp_ids'] = emp_ids
            return JsonResponse({'status': 'ok'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=405)



@csrf_exempt
def get_employee_by_id(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        emp_id = data.get("emp_id")

        try:
            today = date.today()
            emp = (
                Punchdtls1.objects.using('main')
                .filter(id__code=emp_id, dt=today, id__grp1=104, unitname='CUTTING')
                .order_by('id1')
                .first()
            )

            if emp:
                raw_path = emp.id.photo if emp.id and emp.id.photo else None
                if raw_path:
                    filename = raw_path.split('\\')[-1]
                    photo_url = f"https://app.herofashion.com/staff_images/{filename}"
                else:
                    photo_url = ""

                return JsonResponse({
                    "success": True,
                    "name": emp.id.name,
                    "photo": photo_url
                })

            return JsonResponse({"success": False, "message": "Employee not found"})
        
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
    
    return JsonResponse({"success": False, "message": "Invalid request"})


def overwrite(request, id, tableId):
    cutsample = VuePlandtlsTablewise.objects.using('demo').filter(
        tableno=tableId,
        sample_descr__iexact='CUTTING SAMPLE'
    ).order_by('-rownum')
    cutsample_count = cutsample.count()

    orders = VuePlandtlsTablewise.objects.using('demo').filter(
        tableno=tableId,
        sample_descr__iexact='ORDER'
    ).order_by('-rownum')
    order_count = orders.count()

    return render(request, "lay/overwrite.html", {
        'id': id,  # hidden field
        'datas': cutsample,
        'orders': orders,
        'cutsample_count': cutsample_count,
        'order_count': order_count,
        'tableId': tableId,
    })



# def lay_check(request, planno, id):
#     datas = VuePlandetails.objects.using('demo').filter(planno__exact=planno).order_by('-rownum')
#     plan_details = TrsCplan4.objects.using("demo").filter(planno__exact=planno)
#     plan_details_count = TrsCplan4.objects.using("demo").filter(planno__exact=planno).count()
#     if datas:
#         job_no = datas[0].jobno
#         marker_no = datas[0].markerno

#         try:
#             lay_data = lay_data_update.objects.get(
#                 plan_no=planno,
#                 job_no=job_no,
#                 marker_no=marker_no
#             )
#             initial_timer = lay_data.timer  # e.g., "05:12"
#             brown_sheet_timer = lay_data.brown_sheet_timer  # e.g., "01:30"
#             join_marker_timer = lay_data.join_marker_timer
#         except lay_data_update.DoesNotExist:
#             initial_timer = "00:00"
#             brown_sheet_timer = "00:00"
#             join_marker_timer = "00:00"
#     else:
#         job_no = marker_no = ""
#         initial_timer = "00:00"
#         brown_sheet_timer = "00:00"
#         join_marker_timer = "00:00"

#     print("join_marker_timer:", join_marker_timer)
#     print("brown_sheet_timer:", brown_sheet_timer)

#     print("Initial Timer:", initial_timer)
#     return render(request, "lay/lay_check.html", {
#         'datas': datas,
#         'initial_timer': initial_timer,
#         'brown_sheet_timer': brown_sheet_timer,
#         'join_marker_timer': join_marker_timer,
#         'jobno': job_no,
#         'markerno': marker_no,
#         'planno': planno,
#         'id': id,
#         'plan_details': plan_details,
#         "plan_details_count": plan_details_count
#     })


def lay_check(request, planno, id):
    datas = VuePlandetails.objects.using('demo').filter(planno__exact=planno).order_by('-rownum')
    plan_details_qs = TrsCplan4.objects.using("demo").filter(planno__exact=planno)
    plan_details_count = plan_details_qs.count()

    # ✅ Build status for each roll
    roll_status_list = []
    for item in plan_details_qs:
        status = "Complete" if roll_data_update.objects.filter(roll_no__exact=item.rlno,plan_no__exact=planno).exists() else "Pending"
        roll_status_list.append({
            "rlno": item.rlno,
            "ply": item.ply,
            "status": status
        })

    # Get timer values if available
    if datas:
        job_no = datas[0].jobno
        marker_no = datas[0].markerno
        try:
            lay_data = lay_data_update.objects.get(plan_no=planno, job_no=job_no, marker_no=marker_no)
            initial_timer = lay_data.timer
            brown_sheet_timer = lay_data.brown_sheet_timer
            join_marker_timer = lay_data.join_marker_timer
        except lay_data_update.DoesNotExist:
            initial_timer = brown_sheet_timer = join_marker_timer = "00:00"
    else:
        job_no = marker_no = ""
        initial_timer = brown_sheet_timer = join_marker_timer = "00:00"
    
    print("roll_status_list:", roll_status_list)
    return render(request, "lay/lay_check.html", {
        'datas': datas,
        'initial_timer': initial_timer,
        'brown_sheet_timer': brown_sheet_timer,
        'join_marker_timer': join_marker_timer,
        'jobno': job_no,
        'markerno': marker_no,
        'planno': planno,
        'id': id,
        'plan_details': roll_status_list,  # ⬅️ pass status-ready list
        'plan_details_count': plan_details_count
    })


def permissions_view(request, pk=None):
    # Create or get instance for edit
    instance = None
    if pk:
        instance = get_object_or_404(overwrite_permissions, pk=pk)

    if request.method == 'POST':
        if 'delete' in request.POST:
            overwrite_permissions.objects.filter(pk=request.POST.get('delete')).delete()
            return redirect('permissions')

        Emp_id = request.POST.get('Emp_id')
        Password = request.POST.get('Password')

        if pk:
            # Update
            instance.Emp_id = Emp_id
            instance.Password = Password
            instance.save()
        else:
            # Create
            overwrite_permissions.objects.create(Emp_id=Emp_id, Password=Password)

        return redirect('permissions')

    all_permissions = overwrite_permissions.objects.all()
    return render(request, 'lay/permissions.html', {
        'permissions': all_permissions,
        'instance': instance
    })


def validate_overwrite_user(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id")
        password = request.POST.get("password")

        exists = overwrite_permissions.objects.filter(Emp_id=emp_id, Password=password).exists()
        
        return JsonResponse({"valid": exists})

    return JsonResponse({"valid": False}, status=400)


@csrf_exempt
def process_overwrite(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        plans = data.get('plans')
        from_table = data.get('new_table')

        to_table = data.get('old_table')


        for plan_job in plans:
            try:
                planno, jobno = plan_job.split('|')
                VuePlandtlsTablewise.objects.using('demo').filter(
                    planno=planno,
                    jobno=jobno,
                    tableno=from_table
                ).update(tableno=to_table)
            except ValueError:
                continue  # skip invalid data

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'invalid request'}, status=400)


@csrf_exempt
def toggle_table_lock(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id")
        password = request.POST.get("password")

        valid_user = overwrite_permissions.objects.filter(Emp_id=emp_id, Password=password).exists()

        if valid_user:
            # Get or create the lock entry
            lock, created = table_lock.objects.get_or_create(id=1, defaults={
                'table_no_1': False,
                'table_no_2': False
            })

            lock.table_no_1 = not lock.table_no_1  # Toggle
            lock.save()

            return JsonResponse({"success": True, "table_no_1": lock.table_no_1})

        return JsonResponse({"success": False, "error": "Invalid credentials"})

    return JsonResponse({"success": False, "error": "Bad request"}, status=400)


import logging
logger = logging.getLogger(__name__)
logger.warning("Update Timer POST Hit")

@csrf_exempt
def update_timer(request):
    print("Request method:", request.method)
    print("Request body:", request.body)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            plan_no = data.get("plan_no")
            job_no = data.get("job_no")
            marker_no = data.get("marker_no")
            timer = data.get("timer")

            obj, created = lay_data_update.objects.update_or_create(
                plan_no=plan_no,
                job_no=job_no,
                marker_no=marker_no,
                defaults={
                    "timer": timer,
                    "date": date.today()
                }
            )

            return JsonResponse({
                "status": "success",
                "created": created,
                "id": obj.id
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)




@csrf_exempt  # or handle CSRF tokens correctly in frontend
def update_checkbox_timer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            plan_no = data.get('plan_no')
            job_no = data.get('job_no')
            marker_no = data.get('marker_no')
            timer_value = data.get('timer_value')
            timer_column = data.get('timer_column')  # 'brown_sheet_timer' or 'join_marker_timer'

            obj = lay_data_update.objects.get(plan_no=plan_no, job_no=job_no, marker_no=marker_no)

            if timer_column not in ['brown_sheet_timer', 'join_marker_timer']:
                return JsonResponse({'status': 'error', 'message': 'Invalid timer column'}, status=400)

            setattr(obj, timer_column, timer_value)
            obj.save()

            return JsonResponse({'status': 'success', 'message': f'{timer_column} updated'})
        except lay_data_update.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Record not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)


# def roll_datas(request, rlno,plan_no):

#     datas = TrsCplan4.objects.using('demo').filter(rlno__exact=rlno,planno__exact=plan_no)
#     data_list = list(datas.values())
#     return JsonResponse({'datas': data_list})

def roll_datas(request, rlno, plan_no):
    datas = TrsCplan4.objects.using('demo').filter(rlno__exact=rlno, planno__exact=plan_no)
    data_list = list(datas.values())

    if not data_list:
        return JsonResponse({'datas': [], 'message': 'No data found.'}, status=404)

    return JsonResponse({'datas': data_list})


@csrf_exempt  # for AJAX POST without CSRF token (optional, better to use CSRF properly)
def save_roll_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Debugging line
            roll_data_update.objects.create(
                timer = data.get('timer'),
                roll_no = data.get('roll_no'),
                plan_no = data.get('plan_no'),
                job_no = data.get('job_no'),
                f_dia = data.get('f_dia'),
                plan_ply = data.get('plan_ply'),
                plan_obwgt = data.get('plan_obwgt'),
                req_wgt = data.get('req_wgt'),
                actual_dia = data.get('actual_dia'),
                actual_ply = data.get('actual_ply'),
                actual_obwgt = data.get('actual_obwgt'),
                end_bit = data.get('end_bit'),
                bal_wgt = data.get('bal_wgt'),
                scl_wgt = data.get('scl_wgt'),
                remarks = data.get('remarks'),
            )
            return JsonResponse({'success': True, 'message': 'Data saved successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request'})


def get_roll_data_on_load(request):
    plan_no = request.GET.get('plan_no')
    job_no = request.GET.get('job_no')

    if not plan_no or not job_no:
        return JsonResponse({'datas': [], 'count_data': 0})

    datas = roll_data_update.objects.filter(plan_no=plan_no, job_no=job_no)
    datas_count = datas.count()

    data_list = list(datas.values())

    print("Fetched roll data:", data_list)  # Debugging line
    print("Count of roll data:", datas_count)  # Debugging line

    return JsonResponse({
        'datas': data_list,
        'count_data': datas_count
    })

@csrf_exempt
def save_final_plan(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_plan = final_plans.objects.create(
            job_no=data.get("job_no"),
            plan_no=data.get("plan_no"),
            marker_no=data.get("marker_no"),
            lot_no=data.get("lot_no"),
            fabric_color=data.get("fabric_color"),
            timer=data.get("timer"),
        )
        return JsonResponse({"success": True, "id": new_plan.id})

    return JsonResponse({"success": False}, status=400)