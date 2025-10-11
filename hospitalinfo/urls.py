from django.urls import path
from .views import *

app_name='hospitalinfo'

urlpatterns = [
    path('add/',add_hospital,name='add'),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('doctors/',doctors,name='doctors'),
    path('appointment/',appointment,name='appointment'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login')
    
]