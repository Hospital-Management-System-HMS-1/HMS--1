from django.urls import path
from .views import *

app_name='hospitalinfo'

urlpatterns = [
    # hospital urls
    path('hospital_list/',hospital_list,name='hospital_list'),
    path('add/',add_hospital,name='add_hospital'),
    path('delete/<int:hospital_id>/',delete_hospital,name='delete')
]