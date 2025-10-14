from django.urls import path
from .views import *

app_name='HospitalLogin'

urlpatterns=[
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('reset-password/', reset_password, name='reset_password'),
]