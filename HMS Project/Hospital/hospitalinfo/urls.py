from django.urls import path
from .views import *

app_name='hospitalinfo'

urlpatterns = [
    path('add/',add_hospital,name='add'),
]