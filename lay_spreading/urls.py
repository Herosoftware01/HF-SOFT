
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('emp/<int:id>/', views.emp, name='emp'),
    path('task/<int:id>/', views.task, name='task'),
    path('save-emp-ids/', views.save_emp_ids, name='save_emp_ids'),
    path("get-employee/", views.get_employee_by_id, name="get_employee"),
    # path("lay_check/<int:planno>/<int:id>/", views.lay_check, name="lay_check"),
    path("lay_check/<str:planno>/<int:id>/", views.lay_check, name="lay_check"),
    path("overwrite/<int:id>/<int:tableId>/", views.overwrite, name="overwrite"),
    path('permissions/',views.permissions_view, name='permissions'),
    path('permissions/<int:pk>/', views.permissions_view, name='permissions'),
    # path('overwrite_data/<int:pk>/', views.overwrite_data, name='overwrite_data'),
    path("validate-overwrite-user/", views.validate_overwrite_user, name="validate_overwrite_user"),
    path('overwrite/process/', views.process_overwrite, name='process_overwrite'),
    path("toggle-table-lock/", views.toggle_table_lock, name="toggle_table_lock"),
    path('update-timer/', views.update_timer, name='update_timer'),  # ✅ Add this!
    path('update-checkbox-timer/', views.update_checkbox_timer, name='update_checkbox_timer'),
    path('get-roll-data/<str:rlno>/<str:plan_no>/', views.roll_datas, name='roll_datas'),
    path('save-roll-data/', views.save_roll_data, name='save_roll_data'),
    path('get-roll-data-on-load/', views.get_roll_data_on_load, name='get-roll-data-on-load'),
    path('save_final_plan', views.save_final_plan, name='save_final_plan'),
]

    
