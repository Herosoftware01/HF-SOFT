
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from .models import AttUnt,BillAge
from django.db.models import Sum
from datetime import datetime, timedelta
from .models import BillAge
from datetime import datetime, date
from django.db.models import Q
from django.utils import timezone
from .models import VueOverall1,ResignDtls
from django.conf import settings
import os



def get_friday_thursday_range(reference_date=None):
    """Calculate Friday to Thursday range for attendance dashboard"""
    if reference_date is None:
        reference_date = datetime.now().date()
    
    current_weekday = reference_date.weekday()  # Monday=0, Sunday=6
    
    # Calculate last Friday
    if current_weekday >= 4:  # Friday(4) or later (Fri, Sat, Sun)
        days_since_last_friday = current_weekday - 4
    else:  # Monday(0) to Thursday(3)
        days_since_last_friday = current_weekday + 3
    
    last_friday = reference_date - timedelta(days=days_since_last_friday)
    
    # Calculate this Thursday  
    if current_weekday <= 3:  # Monday(0) to Thursday(3)
        days_until_thursday = 3 - current_weekday
    else:  # Friday(4) or later
        days_until_thursday = 10 - current_weekday  # Next week's Thursday
    
    this_thursday = reference_date + timedelta(days=days_until_thursday)
    
    return last_friday, this_thursday

def attendance(request):
    # Get parameters from request
    dept = request.GET.get('dept', 'ALL')
    start_date_str = request.GET.get('startDate')
    end_date_str = request.GET.get('endDate')
    
    # Initialize queryset
    queryset = AttUnt.objects.using('demo').all()
    
    # Filter by department
    if dept:
        queryset = queryset.filter(dept__iexact=dept)
    
    # Handle date range - default to Friday-Thursday if not provided
    if not start_date_str or not end_date_str:
        # Use Friday-Thursday default range
        start_date, end_date = get_friday_thursday_range()
    else:
        # Parse provided dates
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            # Fallback to default range if date parsing fails
            start_date, end_date = get_friday_thursday_range()
    
    # Filter queryset by date range
    queryset = queryset.filter(Date__range=[start_date, end_date])
    
    # Aggregate data by date
    data_qs = queryset.values('Date').annotate(
        total=Sum('onroll'),
        present=Sum('present'),
        absent=Sum('absent')
    ).order_by('Date')
    
    # Prepare response data
    if not data_qs.exists():
        # No data found - return empty structure
        response_data = [{
            "unit": dept,
            "date": str(datetime.now().date()),
            "present": 0,
            "absent": 0,
            "total": 0,
            "present_pct": 0,
            "absent_pct": 0,
        }]
    else:
        response_data = []
        for row in data_qs:
            total = row['total'] or 0
            present = row['present'] or 0
            absent = row['absent'] or 0
            
            # Calculate percentages
            present_pct = round((present / total) * 100) if total > 0 else 0
            absent_pct = round((absent / total) * 100) if total > 0 else 0
            
            response_data.append({
                "unit": dept,
                "date": row['Date'].strftime("%Y-%m-%d"),
                "present": present,
                "absent": absent,
                "total": total,
                "present_pct": present_pct,
                "absent_pct": absent_pct,
            })
    
    # Render template with context
    context = {
        "data": response_data,
        "unit": dept,
        "default_start": start_date.strftime("%Y-%m-%d"),
        "default_end": end_date.strftime("%Y-%m-%d"),
    }
    
    return render(request, "attendance.html", context)




def oneday(request):
    day_str = request.GET.get('date')
    if day_str:
        try:
            day = datetime.strptime(day_str, "%Y-%m-%d").date()
        except ValueError:
            day = datetime.now().date()
    else:
        day = datetime.now().date()

    # Fetch all distinct units (for filter dropdown)
    all_units = AttUnt.objects.using("demo").values_list("dept", flat=True).distinct().order_by("dept")

    # Apply unit filter (default: ALL)
    dept_filter = request.GET.get('dept', 'ALL')
    queryset = AttUnt.objects.using("demo").filter(Date=day)
    if dept_filter != 'ALL':
        queryset = queryset.filter(dept__iexact=dept_filter)

    # Group by units (departments)
    units_qs = queryset.values('dept').annotate(
        total=Sum('onroll'),
        present=Sum('present'),
        absent=Sum('absent'),
    ).order_by('dept')

    # Prepare data for template
    unit_data = []
    for row in units_qs:
        total = row['total'] or 0
        present = row['present'] or 0
        absent = row['absent'] or 0
        present_pct = round((present / total) * 100, 1) if total > 0 else 0
        absent_pct = round((absent / total) * 100, 1) if total > 0 else 0
        unit_data.append({
            'unit': row['dept'],
            'total': total,
            'present': present,
            'absent': absent,
            'present_pct': present_pct,
            'absent_pct': absent_pct,
        })

    return render(request, 'oneday.html', {
    "unit_data": unit_data,
    "day": day.strftime("%d-%m-%Y"),
    "unit": dept_filter,   # 👈 now matches your template
    })






def report(request):
    datas = VueOverall1.objects.using('demo1').all()
    job_datas = datas.values_list('jobno', flat=True).distinct().order_by('jobno')
    merch_datas = datas.values_list('o_merch', flat=True).distinct().order_by('o_merch')

    # print(" Job Datas:", job_datas)

    search = request.GET.get('search', '')
    unit = request.GET.get('unit', '')
    jobno = request.GET.get('jobno', '')
    merch = request.GET.get('merch', '')

    if search:
        datas = datas.filter(jobno__icontains=search) | datas.filter(o_merch__icontains=search) | datas.filter(clr__icontains=search)

    if unit and unit != "ALL":
        datas = datas.filter(unit=unit)

    if jobno:
        datas = datas.filter(jobno=jobno)

    if merch:
        datas = datas.filter(o_merch=merch)

    data_count = datas.count()


    for order in datas:
        if order.Image:
            filename = os.path.basename(order.Image)
            order.Image = f"https://app.herofashion.com/pro_image/{filename}"
        else:
            order.Image = None
  

    return render(request, 'stock.html', {
        'datas': datas,
        'data_count': data_count,
        'job_datas': job_datas,
        'merch_datas': merch_datas,
    })


def bill(request):
    # Get all BillAge objects from the mssql database
    datas = BillAge.objects.using('demo1').all()
    
    # Get filter parameters from GET request
    employee_filter = request.GET.get('employees', '')
    module = request.GET.get('module', '')
    from_date = request.GET.get('from_date', '')
    to_date = request.GET.get('to_date', '')
    aging_range = request.GET.get('aging_range', '')
    min_aging = request.GET.get('min_aging', '')
    
    # Create a copy for dropdown population (before final filtering)
    dropdown_data = datas
    
    # Apply employee filter
    if employee_filter and employee_filter != "ALL":
        try:
            employee_id = int(employee_filter)
            # First get all unique employee names to match ID
            all_employee_names = list(datas.values_list('employees', flat=True).distinct().order_by('employees'))
            all_employee_names_filtered = [name for name in all_employee_names if name is not None and name.strip()]
            
            if employee_id <= len(all_employee_names_filtered):
                employee_name = all_employee_names_filtered[employee_id - 1]
                datas = datas.filter(employees=employee_name)
                dropdown_data = dropdown_data.filter(employees=employee_name)
        except (ValueError, IndexError):
            pass
    
    # Apply module filter
    if module and module != "ALL" and module:
        datas = datas.filter(module=module)
        dropdown_data = dropdown_data.filter(module=module)
    
    # Apply date range filter on billdate
    if from_date:
        try:
            start_date = datetime.strptime(from_date, '%Y-%m-%d').date()
            datas = datas.filter(billdate__date__gte=start_date)
            dropdown_data = dropdown_data.filter(billdate__date__gte=start_date)
        except ValueError:
            pass
    
    if to_date:
        try:
            end_date = datetime.strptime(to_date, '%Y-%m-%d').date()
            datas = datas.filter(billdate__date__lte=end_date)
            dropdown_data = dropdown_data.filter(billdate__date__lte=end_date)
        except ValueError:
            pass
    
    # Now populate dropdowns based on filtered data for interdependency
    # Get distinct values for module dropdown filter (based on current filters)
    if employee_filter and employee_filter != "ALL":
        # If employee is selected, show only modules for that employee
        module_datas = dropdown_data.values_list('module', flat=True).distinct().order_by('module')
    else:
        # If no employee selected, show all modules
        module_datas = BillAge.objects.using('demo1').values_list('module', flat=True).distinct().order_by('module')
    
    # Get employees for dropdown (based on current module filter if any)
    if module and module != "ALL":
        # If module is selected, show only employees for that module
        employee_names = dropdown_data.values_list('employees', flat=True).distinct().order_by('employees')
    else:
        # If no module selected, show all employees
        employee_names = BillAge.objects.using('demo1').values_list('employees', flat=True).distinct().order_by('employees')
    
    # Filter out None/null values and create employee list
    employee_names_filtered = [name for name in employee_names if name is not None and name.strip()]
    employees = []
    for idx, name in enumerate(employee_names_filtered, 1):
        employees.append({'id': idx, 'name': name})
    
    # Calculate aging in Python after database query
    data_list = []
    
    for idx, item in enumerate(datas, 1):       
        try:
            # Extract and normalize bill_date
            bill_date = None
            if hasattr(item.billdate, 'date'):
                bill_date = item.billdate.date()
            elif isinstance(item.billdate, (date, datetime)):
                bill_date = item.billdate if isinstance(item.billdate, date) else item.billdate.date()
            elif isinstance(item.billdate, str) and item.billdate.strip():
                try:
                    bill_date = datetime.strptime(item.billdate.strip(), '%Y-%m-%d').date()
                except ValueError:
                    bill_date = datetime.strptime(item.billdate.strip(), '%d-%m-%Y').date()
            
            # Extract and normalize edate (less_date)
            less_date = None
            if hasattr(item.edate, 'date'):
                less_date = item.edate.date()
            elif isinstance(item.edate, (date, datetime)):
                less_date = item.edate if isinstance(item.edate, date) else item.edate.date()
            elif isinstance(item.edate, str) and item.edate.strip():
                try:
                    less_date = datetime.strptime(item.edate.strip(), '%Y-%m-%d').date()
                except ValueError:
                    less_date = datetime.strptime(item.edate.strip(), '%d-%m-%Y').date()
            
            # Only calculate if both dates exist
            if bill_date and less_date:
                aging_days = (less_date - bill_date).days
            else:
                aging_days = None
            
            print(f"Debug: less_date={less_date}, bill_date={bill_date}, aging_days={aging_days}")
            
            # Add calculated aging and serial number to the object
            item.calculated_aging = aging_days
            item.br_ageing = aging_days
            item.billdate_ageing = aging_days
            item.no = idx
            
            data_list.append(item)
            
        except (ValueError, AttributeError, TypeError) as e:
            print(f"Error calculating aging for item {idx}: {e}")
            item.calculated_aging = 0
            item.br_ageing = 0
            item.billdate_ageing = 0
            item.no = idx
            data_list.append(item)
    
    # Apply minimum aging filter
    if min_aging:
        try:
            min_days = int(min_aging)
            data_list = [item for item in data_list if item.calculated_aging >= min_days]
        except ValueError:
            pass
    
    # Apply hardcoded filter (aging >= 1 days)
    data_list = [item for item in data_list if item.calculated_aging is not None and item.calculated_aging >= 1]
    
    # Apply aging range filter
    if aging_range:
        filtered_data = []
        for item in data_list:
            aging = item.calculated_aging or 0
            
            if aging_range == '7-30' and 7 <= aging <= 30:
                filtered_data.append(item)
            elif aging_range == '31-60' and 31 <= aging <= 60:
                filtered_data.append(item)
            elif aging_range == '61-90' and 61 <= aging <= 90:
                filtered_data.append(item)
            elif aging_range == '91-180' and 91 <= aging <= 180:
                filtered_data.append(item)
            elif aging_range == '180+' and aging > 180:
                filtered_data.append(item)
        
        data_list = filtered_data
    
    # Sort by module (ascending) first, then by aging (descending)
    data_list.sort(key=lambda x: (x.module or '', -(x.calculated_aging or 0)))
    
    # Renumber after filtering and sorting
    for idx, item in enumerate(data_list, 1):
        item.no = idx
    
    # Count filtered results
    data_count = len(data_list)
    
    return render(request, 'bill.html', {
        'datas': data_list,
        'data_count': data_count,
        'module_datas': module_datas,
        'employees': employees,
        'selected_incharge': employee_filter,
        'selected_module': module,
        'selected_from_date': from_date,
        'selected_to_date': to_date,
        'selected_aging_range': aging_range,
        'selected_min_aging': min_aging,
    })


def resign_report(request):
    unit_filter = request.GET.get('unit', 'ALL')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    resign = ResignDtls.objects.using('main').all()

    if unit_filter and unit_filter != 'ALL':
        resign = resign.filter(dept=unit_filter)

    # Compute current month bounds
    today = timezone.now().date()
    first_day_of_month = today.replace(day=1)

    # Default to this month if no dates provided
    if not from_date and not to_date:
        resign = resign.filter(resigndt__date__range=(first_day_of_month, today))
        effective_from = first_day_of_month
        effective_to = today
    else:
        if from_date and to_date:
            resign = resign.filter(resigndt__date__range=(from_date, to_date))
            effective_from = from_date
            effective_to = to_date
        elif from_date:
            resign = resign.filter(resigndt__date__gte=from_date)
            effective_from = from_date
            effective_to = None
        else:  # only to_date
            resign = resign.filter(resigndt__date__lte=to_date)
            effective_from = None
            effective_to = to_date

    resign = resign.order_by('-resigndt')

    for order in resign:
        if getattr(order, 'photo', None):
            filename = os.path.basename(order.photo)
            if settings.DEBUG:
                order.photo = f"http://app.herofashion.com/staff_images/{filename}"
        else:
            order.photo = None

    total_resignations = resign.count()

    avg_days = 0
    if total_resignations > 0:
        total_days = sum([r.days_worked for r in resign if getattr(r, 'days_worked', None)])
        avg_days = int(total_days / total_resignations) if total_days > 0 else 0

    # This month count (based on calendar month regardless of filters)
    this_month_count = ResignDtls.objects.using('main') \
        .filter(resigndt__date__gte=first_day_of_month, resigndt__date__lte=today) \
        .count()

    departments = ResignDtls.objects.using('main') \
        .values_list('dept', flat=True).distinct().order_by('dept')

    context = {
        'resign': resign,
        'departments': departments,
        'unit': unit_filter,
        'from_date': effective_from if not from_date and not to_date else from_date,
        'to_date': effective_to if not from_date and not to_date else to_date,
        'total_resignations': total_resignations,
        'avg_days': avg_days,
        'this_month_count': this_month_count,
    }

    return render(request, 'regin.html', context)