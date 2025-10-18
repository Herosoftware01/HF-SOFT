from django.urls import path
from .import views

app_name = 'attendance'

urlpatterns = [
    path('', views.attendance, name='attendance'),
    path('oneday/', views.oneday, name='oneday'),
    path('report/', views.report, name='report'),
    path('bill/', views.bill, name='bill'),
    path('resign_report/',views.resign_report,name='resign_report'),
    path('join/',views.join_data,name='join'),
]
