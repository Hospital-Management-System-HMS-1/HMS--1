from django.urls import path
from . import views

app_name = 'hospitalinfo'

urlpatterns = [
    # Hospital
    path('hospital_list/', views.hospital_list, name='hospital_list'),
    path('add_hospital/', views.add_hospital, name='add_hospital'),
    path('update_hospital/<int:hospital_id>/', views.update_hospital, name='update_hospital'),
    path('delete_hospital/<int:hospital_id>/', views.delete_hospital, name='delete_hospital'),

    # Doctor
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('update_doctor/<int:doctor_id>/', views.update_doctor, name='update_doctor'),
    path('delete_doctor/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),

    # Department
    path('depart_list/', views.depart_list, name='depart_list'),
    path('add_depart/', views.add_depart, name='add_depart'),
    path('update_depart/<int:depart_id>/', views.update_depart, name='update_depart'),
    path('delete_depart/<int:depart_id>/', views.delete_depart, name='delete_depart'),

    # Appointment
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('update_appointment/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
]
