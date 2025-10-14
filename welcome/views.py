# welcome/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserPermission,VueOverall1,OrdOrderOms,EmpAttendanceFact,OrdMaterialplanPen,FabKnitprgvsrecd,OrdStk,FabFabricStatus,GeneralDeliveryReport,FabYarn,FabKnitprgvsrecd,YarnPovspi,PrintRgbAlt,AllotPen
import json
import pandas as pd
import numpy as np
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.clickjacking import xframe_options_exempt

@login_required
def welcome(request):
    return render(request, 'welcome.html')


def user_list (request):
    users = User.objects.all()
    return render(request, 'welcome/user_list.html', {'users': users})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("Authenticated User:", user)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'welcome/login.html')


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

@csrf_exempt  # Disable CSRF for API usage – only do this if you're not using session authentication from browsers
def login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON payload
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'error': 'Username and password are required.'}, status=400)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Login successful', 'username': user.username}, status=200)
            else:
                return JsonResponse({'error': 'Invalid username or password.'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)

    return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    return render(request, 'welcome/register.html')

@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.all()

    if request.method == 'POST':
        for user in users:
            perm, created = UserPermission.objects.get_or_create(user=user)
            perm.can_access_admin = bool(request.POST.get(f'admin_{user.id}', False))
            perm.can_access_roll = bool(request.POST.get(f'roll_{user.id}', False))
            perm.can_access_attendance = bool(request.POST.get(f'attendance_{user.id}', False))
            perm.powerbi_data = bool(request.POST.get(f'powerbi_data_{user.id}', False))
            perm.production_data = bool(request.POST.get(f'production_data_{user.id}', False))
            perm.lay_spreading = bool(request.POST.get(f'lay_spreading_{user.id}', False))
            perm.lay_admin = bool(request.POST.get(f'lay_admin_{user.id}', False))
            perm.unit1 = bool(request.POST.get(f'unit1_{user.id}', False))
            perm.unit2 = bool(request.POST.get(f'unit2_{user.id}', False))
            perm.unit3 = bool(request.POST.get(f'unit3_{user.id}', False))
            perm.unit4 = bool(request.POST.get(f'unit4_{user.id}', False))
            perm.unit5 = bool(request.POST.get(f'unit5_{user.id}', False))
            perm.merch1 = bool(request.POST.get(f'merch1_{user.id}', False))
            perm.merch2 = bool(request.POST.get(f'merch2_{user.id}', False))
            perm.server13 = bool(request.POST.get(f'server13_{user.id}', False))
            perm.server10 = bool(request.POST.get(f'server10_{user.id}', False))
            perm.server15 = bool(request.POST.get(f'server15_{user.id}', False))
            perm.save()
        messages.success(request, "Permissions updated successfully.")
        return redirect('user_list')

    
    permissions = {u.id: UserPermission.objects.get_or_create(user=u)[0] for u in users}

    return render(request, 'welcome/user_list.html', {'users': users, 'permissions': permissions})



def apk_download(request):
    return render(request, 'powerbi/apk_download.html')

def order(request):
    return render(request, 'powerbi/order.html')



@xframe_options_exempt
def server13(request):
    return render(request, 'powerbi/server13.html')

@xframe_options_exempt
def server15(request):
    return render(request, 'powerbi/server13.html')

@xframe_options_exempt
def server10(request):
    return render(request, 'powerbi/server13.html')

def fab_table(request):
    return render(request, 'powerbi/fab.html')

def orderst(request):
    return render(request, 'powerbi/orderst.html')

def empatt(request):
    return render(request, 'powerbi/empatt.html')

def fabmatpen1(request):
    return render(request, 'powerbi/Fabmatpen.html')

def sample_data(request):
    return render(request, 'powerbi/sample_data.html')

# def Allot(request):
#     return render(request, 'powerbi/Allotpen.html')


def unit1(request):
    # Fetch only UNIT-1 data
    datas = VueOverall1.objects.using('demo1').filter(unit='UNIT-1')

    for emp in datas:
        # raw_path = emp.id.photo
        raw_path = emp.Image if emp.Image and emp.Image else None
        if raw_path:
            # Extract filename
            filename = raw_path.split('\\')[-1]
            emp.Image = f"https://app.herofashion.com/staff_images/{filename}"
            # print(f"Employee: {emp.name}, Photo URL: {emp.photo_url}")
        else:
            emp.Image = ""  # fallback if no image

    # Convert queryset to list of dictionaries for JSON use in template
    datas_json = json.dumps(list(datas.values()))

    return render(request, 'powerbi/unit1.html', {'datas_json': datas_json})


def unit2(request):
    datas = VueOverall1.objects.using('demo1').filter(unit='UNIT-2')
    datas_json = json.dumps(list(datas.values()))
    return render(request, 'powerbi/unit2.html', {'datas_json': datas_json})

def unit3(request):
    datas = VueOverall1.objects.using('demo1').filter(unit='UNIT-3')
    datas_json = json.dumps(list(datas.values()))
    return render(request, 'powerbi/unit3.html', {'datas_json': datas_json})

def unit4(request):
    datas = VueOverall1.objects.using('demo1').filter(unit='UNIT-4')
    datas_json = json.dumps(list(datas.values()))
    return render(request, 'powerbi/unit4.html', {'datas_json': datas_json})


def panda(request):
    queryset = VueOverall1.objects.using('demo1').values()

    # Modify image paths
    for obj in queryset:
        raw_path = obj['Image'] if obj.get('Image') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['Image'] = f"https://app.herofashion.com/pro_image/{filename}"
        else:
            obj['Image'] = ""

    # Optional: Load to DataFrame if you need Pandas features
    df = pd.DataFrame.from_records(queryset)
    # Convert to JSON-serializable format
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)

def panda_html(request):
    return render(request, 'powerbi/pandas.html')
    

def order_panda(request):
    queryset = OrdOrderOms.objects.using('demo1').values()

    # Modify image paths
    for obj in queryset:
        raw_path = obj['mainimagepath'] if obj.get('mainimagepath') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['mainimagepath'] = f"https://app.herofashion.com/all_image/{filename}"
        else:
            obj['mainimagepath'] = ""

    # Optional: Load to DataFrame if you need Pandas features
    df = pd.DataFrame.from_records(queryset)

    # Convert to JSON-serializable format
    data = df.to_dict(orient='records')

    return JsonResponse(data, safe=False)


def Order_panda_html(request):
    return render(request, 'powerbi/order_pandas.html')



def testing_api(request):
    queryset = EmpAttendanceFact.objects.using('demo1').values()
    # Modify image paths
    for obj in queryset:
        raw_path = obj['img'] if obj.get('img') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['img'] = f"https://app.herofashion.com/staff_images/{filename}"
        else:
            obj['img'] = ""

    # Optional: Load to DataFrame if you need Pandas features
    df = pd.DataFrame.from_records(queryset)

    # Convert to JSON-serializable format
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)

def testing (request):
    return render(request,"powerbi/testing.html")

def res (request):
    return render(request,"powerbi/responsive.html")



def ordmatpen(request):
   
    queryset = OrdMaterialplanPen.objects.using('demo1').values()

    df = pd.DataFrame.from_records(queryset)

    # Convert to JSON-serializable format
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)

def ordmatpen1(request):
 
    return render(request, "powerbi/Fabmatpenresponse.html")


def fab(request):
   
    queryset = FabKnitprgvsrecd.objects.using('demo1').values()
    for obj in queryset:
        raw_path = obj['img_fpath'] if obj.get('img_fpath') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['img_fpath'] = f"https://app.herofashion.com/staff_images/{filename}"
        else:
            obj['img_fpath'] = ""

    df = pd.DataFrame.from_records(queryset)

    # Convert to JSON-serializable format
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)

def ordst_api(request):
    queryset = OrdStk.objects.using('demo1').values()

    # Modify image paths
    for obj in queryset:
        raw_path = obj['orderimage'] if obj.get('orderimage') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['orderimage'] = f"https://app.herofashion.com/all_image/{filename}"
        else:
            obj['orderimage'] = ""

    # Optional: Load to DataFrame if you need Pandas features
    df = pd.DataFrame.from_records(queryset)

    # Convert to JSON-serializable format
    data = df.to_dict(orient='records')

    return JsonResponse(data, safe=False)


def General(request):
    queryset = GeneralDeliveryReport.objects.using('demo1').values()
    df = pd.DataFrame.from_records(queryset)

    # Replace NaN/NaT with None so JSON is valid
    df = df.replace({np.nan: None, pd.NaT: None})

    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)

def General1(request): 
    return render(request, "powerbi/General.html")


 

def Fabst(request):
    queryset = FabFabricStatus.objects.using('demo1').values()
    df = pd.DataFrame.from_records(queryset)
    df = df.replace({np.nan: None, pd.NaT: None})
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)


def Fabst1(request):
    return render(request, "powerbi/fabst.html")



def Fabyarn(request):
    queryset = FabYarn.objects.using('demo1').values()

    for obj in queryset:
        raw_path = obj['mainimagepath'] if obj.get('mainimagepath') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['mainimagepath'] = f"https://app.herofashion.com/all_image/{filename}"
        else:
            obj['mainimagepath'] = ""

    df = pd.DataFrame.from_records(queryset)
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)
 

def Fabyarn1(request):
    return render(request, "powerbi/Fabyarn.html")


def fabKnitprgvsrec(request):
    queryset = FabKnitprgvsrecd.objects.using('demo1').values()

    for obj in queryset:
        raw_path = obj['img_fpath'] if obj.get('img_fpath') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['img_fpath'] = f"https://app.herofashion.com/all_image/{filename}"
        else:
            obj['img_fpath'] = ""

    df = pd.DataFrame.from_records(queryset)
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)
 

def fabKnitprgvsrec1(request):
    return render(request, "powerbi/Fabknit.html")


def YarnPovspinew(request):
    queryset = YarnPovspi.objects.using('demo1').values()

    for obj in queryset:
        raw_path = obj['img_fpath'] if obj.get('img_fpath') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['img_fpath'] = f"https://app.herofashion.com/all_image/{filename}"
        else:
            obj['img_fpath'] = ""

    df = pd.DataFrame.from_records(queryset)

    # Replace NaN/NaT with None so JSON is valid
    df = df.replace({np.nan: None, pd.NaT: None})

    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)
 
def YarnPovspi1(request):
    return render(request, "powerbi/Yarnpopi.html")

def PrintRgb(request):
    queryset = PrintRgbAlt.objects.using('demo1').values()

    for obj in queryset:
        raw_path = obj['img_fpath'] if obj.get('img_fpath') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['img_fpath'] = f"https://app.herofashion.com/all_image/{filename}"
        else:
            obj['img_fpath'] = ""

    df = pd.DataFrame.from_records(queryset)

    # Replace NaN/NaT with None so JSON is valid
    df = df.replace({np.nan: None, pd.NaT: None})
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)

def PrintRgb1(request):
    return render(request, "powerbi/Printing.html")

def Allotpen(request):
    queryset = AllotPen.objects.using('demo1').values()

    for obj in queryset:
        raw_path = obj['mainimagepath'] if obj.get('mainimagepath') else None
        if raw_path:
            filename = raw_path.split('\\')[-1]
            obj['mainimagepath'] = f"https://app.herofashion.com/all_image/{filename}"
        else:
            obj['mainimagepath'] = ""

    df = pd.DataFrame.from_records(queryset)
    data = df.to_dict(orient='records')
    return JsonResponse(data, safe=False)


def Allotpen1(request):
    return render(request, "powerbi/Allotpen.html")