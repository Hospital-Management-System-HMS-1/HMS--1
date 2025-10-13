from django.urls import path
from .views import *

app_name = 'hospitalinfo'

urlpatterns = [

    path('hospital_list/', hospital_list, name='hospital_list'),
    path('add_hospital/', add_hospital, name='add_hospital'),
    path('update_hospital/<int:hospital_id>/', update_hospital, name='update_hospital'),
    path('delete_hospital/<int:hospital_id>/', delete_hospital, name='delete_hospital'),


    path('depart_list/', depart_list, name='depart_list'),
    path('add_depart/', add_department, name='add_depart'),
    path('update_depart/<int:dept_id>/', update_depart, name='update_depart'),
    path('delete_depart/<int:dept_id>/', delete_depart, name='delete_depart'),

    path('doctor_list/', doctor_list, name='doctor_list'),          
    path('add_doctor/', add_doctor, name='add_doctor'),             
    path('update_doctor/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path('delete_doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),  
]
