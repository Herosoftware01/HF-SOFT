
from django.contrib import admin
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = 'roll'

urlpatterns = [
    path('home/<int:machine_id>/', views.home, name='home'),
    # path('login/', views.custom_login, name='login'),
    path('', views.group_card_selection, name='group_login_page'), 
    path('machine/<int:machine_id>/', views.machine_jobs, name='machine_jobs'),
    # path('logout/', views.custom_logout, name='logout'),
    path('save-roll-update/', views.save_roll_update, name='save_roll_update'),
    # path('save_roll_timer_update/', views.save_roll_timer_update, name='save_roll_timer_update'),
    # path('fetch_roll_details/', views.fetch_roll_details, name='fetch_roll_details'),
    path('manifest.json', views.manifest, name='manifest'),
    path('fetch-roll-data/<str:roll_no>/', views.fetch_roll_data, name='fetch_roll_data'),
    # path('fetch-roll-data/<str:roll_no>/', views.fetch_roll_data, name='fetch_roll_data'),
    # path('fetch-roll-data/', views.fetch_roll_data, name='fetch_roll_data'),
    path('submit_mistake/', views.submit_mistake, name='submit_mistake'),
    path('upload-images/', views.upload_images, name='upload_images'),
    path('view-images/', views.view_images, name='view_images'),
    path('save-final-data/', views.save_final_data, name='save_final_data'),
    path('roll_report/', views.roll_report, name='roll_report'),
    path('delete-roll/', views.delete_roll, name='delete_roll'),
    
    path('machine_report/<int:machine_id>/', views.machine_report, name='machine_report'),

    path('check_roll_exists/', views.check_roll_exists, name='check_roll_exists'),
    path('validate_user/', views.validate_user, name='validate_user'),
    path('fetch_roll_details/', views.fetch_roll_details, name='fetch_roll_details'),
    path('break/', views.break_screen, name='break_screen'),
    path('api/break-status/', views.get_current_break, name='break_status'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STAFF_IMAGES_URL, document_root=settings.STAFF_IMAGES_ROOT)
    urlpatterns += static(settings.ORDER_IMAGES_URL, document_root=settings.ORDER_IMAGES_ROOT)