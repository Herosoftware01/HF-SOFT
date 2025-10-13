
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from .models import AttUnt
from django.db.models import Sum
from datetime import datetime, timedelta


from .models import VueOverall1
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
            order.Image = f"https://g5s2jh39-7004.inc1.devtunnels.ms/pro_image/{filename}"
        else:
            order.Image = None
  

    return render(request, 'stock.html', {
        'datas': datas,
        'data_count': data_count,
        'job_datas': job_datas,
        'merch_datas': merch_datas,
    })



