from django.urls import path
from .views import home, signup, login, logout, resetpassword

app_name = "HospitalLogin"

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("reset-password/", resetpassword, name="resetpassword"),
]
