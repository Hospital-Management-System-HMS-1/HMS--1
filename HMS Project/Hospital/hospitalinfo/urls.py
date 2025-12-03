from django.urls import path
from .views import *

app_name = 'hospitalinfo'

urlpatterns = [
    path('hospital_list/', hospital_list, name='hospital_list'),
    path('add_hospital/', add_hospital, name='add_hospital'),
    path('update_hospital/<int:hospital_id>/', update_hospital, name='update_hospital'),
    path('delete_hospital/<int:hospital_id>/', delete_hospital, name='delete_hospital'),

    path('doctor_list/', doctor_list, name='doctor_list'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('update_doctor/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path('delete_doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),

    path('depart_list/', depart_list, name='depart_list'),
    path('add_depart/', add_depart, name='add_depart'),
    path('update_depart/<int:depart_id>/', update_depart, name='update_depart'),
    path('delete_depart/<int:depart_id>/', delete_depart, name='delete_depart'),

    path('appointment_list/', appointment_list, name='appointment_list'),
    path('add_appointment/', add_appointment, name='add_appointment'),
    path('update_appointment/<int:appointment_id>/', update_appointment, name='update_appointment'),
    path('delete_appointment/<int:appointment_id>/', delete_appointment, name='delete_appointment'),

    path('patient_list/', patient_list, name='patient_list'),
    path('add_patient/', add_patient, name='add_patient'),
    path('update_patient/<int:patient_id>/', update_patient, name='update_patient'),
    path('delete_patient/<int:patient_id>/', delete_patient, name='delete_patient'),

    path('specialist_list/', specialist_list, name='specialist_list'),
    path('add_specialist/', add_specialist, name='add_specialist'),
    path('update_specialist/<int:specialist_id>/', update_specialist, name='update_specialist'),
    path('delete_specialist/<int:specialist_id>/', delete_specialist, name='delete_specialist'),

    path('doctorspecialty_list/', doctorSpecialty_list, name='doctorspecialty_list'),
    path('add_doctorspecialty/', add_doctorspecialty, name='add_doctorspecialty'),
    path('update_doctorspecialty/<int:doctorspecialty_id>/', update_doctorspecialty, name='update_doctorspecialty'),
    path('delete_doctorspecialty/<int:doctorspecialty_id>/', delete_doctorspecialty, name='delete_doctorspecialty'),
]
