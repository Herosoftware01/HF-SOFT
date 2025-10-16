# navapp/urls.py
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.welcome, name='welcome'),  # admin welcome
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('user_list/', views.user_list, name='user_list'),
    path('order/', views.order, name='order'),
    path('ordst_api/', views.ordst_api, name='ordst_api'),
    path('fab_table/', views.fab_table, name='fab_table'),
    path('orderst/', views.orderst, name='orderst'),
    path('empatt/', views.empatt, name='empatt'),
    path('Fabmatpen/', views.fabmatpen1, name='fabmatpen'),
    path('Allotpen/', views.Allotpen, name='Allot'),
    path('Allotpen1/', views.Allotpen1, name='Allot'),
    path('unit1/', views.unit1, name='unit1'),
    path('unit2/', views.unit2, name='unit2'),
    path('unit3/', views.unit3, name='unit3'),
    path('unit4/', views.unit4, name='unit4'),
    path('apk_download/', views.apk_download, name='apk_download'),
    path('panda/', views.panda, name='panda'),
    path('panda_html/', views.panda_html, name='panda_html'),
    path('order_panda/', views.order_panda, name='order_panda'),
    path('Order_panda_html/', views.Order_panda_html, name='Order_panda_html'),
    path('testing/', views.testing, name='testing'),
    path('testing_api/', views.testing_api, name='testing_api'),
    path('ordmatpen1/', views.ordmatpen1, name='ordmatpen'),
    path('ordmatpen/', views.ordmatpen, name='ordmatpen'),
    path('iframe_report/', views.iframe_report, name='iframe_report'),
    path('res/', views.res, name='res'),
    path('fab/', views.fab, name='fab'),
    path('General/', views.General, name='General'),
    path('General1/', views.General1, name='General1'),
    path('Fabst/', views.Fabst, name='Fabst'),
    path('Fabst1/', views.Fabst1, name='Fabst1'),
    path('Fabyarn/', views.Fabyarn, name='Fabyarn'),
    path('Fabyarn1/', views.Fabyarn1, name='Fabyarn1'),
    path('fabKnitprgvsrec/', views.fabKnitprgvsrec, name='fabKnitprgvsrec'),
    path('fabKnitprgvsrec1/', views.fabKnitprgvsrec1, name='fabKnitprgvsrec1'),
    path('YarnPovspinew/', views.YarnPovspinew, name='YarnPovspinew'),
    path('YarnPovspi1/', views.YarnPovspi1, name='YarnPovspi1'),
    path('PrintRgb/', views.PrintRgb, name='PrintRgb'),
    path('PrintRgb1/', views.PrintRgb1, name='PrintRgb1'),
    path('server13/', views.server13, name='server13'),
    path('server15/', views.server15, name='server15'),
    path('server10/', views.server10, name='server10'),
    path('api/login/', views.login_api, name='api_login'),
    path('sample_data/', views.sample_data, name='sample_data'),
<<<<<<< HEAD
    path('non_pandas/', views.non_pandas, name='non_pandas'),
    path('non_pandas_1/', views.non_pandas_1, name='non_pandas_1'),
=======
    path('Ordsampst/', views.Ordsampst, name='Ordsampst'),
    path('Ordsampst1/', views.Ordsampst1, name='Ordsampst'),
>>>>>>> 4ec96b8b9eac41f09864ff34f96b8d44e9830d2a
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STAFF_IMAGES_URL, document_root=settings.STAFF_IMAGES_ROOT)
    urlpatterns += static(settings.ORDER_IMAGES_URL, document_root=settings.ORDER_IMAGES_ROOT)
    urlpatterns += static(settings.PRO_URL, document_root=settings.PRO_ROOT)
    urlpatterns += static(settings.ALL_URL, document_root=settings.ALL_ROOT)