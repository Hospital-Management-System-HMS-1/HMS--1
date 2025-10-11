from django.urls import path
from .views import *

app_name='hospitalinfo'

urlpatterns = [
    # hospital urls
    path('hospital_list/',hospital_list,name='hospital_list'),
    path('add_hospital/',add_hospital,name='add_hospital'),
    path('delete_hospital/<int:hospital_id>/',delete_hospital,name='delete_hospital'),
    path('update_hospital/<int:hospital_id>/',update_hospital,name='update_hospital'),
    # department Urls
    path('depart_list/',depart_list,name='depart_list'),
    path('add_depart/',add_department,name='add_depart'),
    path('update_depart/<int:dept_id>/',update_depart,name='update_depart'),
    path('delete_depart/<int:dept_id>/',delete_depart,name='delete_depart')
]