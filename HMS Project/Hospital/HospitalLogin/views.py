from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import signupForm, loginForm, ResetPasswordForm


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("HospitalLogin:login")
    else:
        form = signupForm()
    return render(request, "signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data["username"]
            psw = form.cleaned_data["password"]
            user = authenticate(username=uname, password=psw)
            if user is not None:
                auth_login(request, user)
                next_url = request.GET.get("next") or "HospitalLogin:home"
                return redirect(next_url)
            form.add_error(None, "Invalid username and password")
    else:
        form = loginForm()
    return render(request, "login.html", {"form": form})


def logout(request):
    auth_logout(request)
    return redirect("HospitalLogin:home")


def resetpassword(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                messages.success(request, "Password updated successfully. You can login now.")
                return redirect("HospitalLogin:login")
            except User.DoesNotExist:
                form.add_error("username", "Username does not exist.")
    else:
        form = ResetPasswordForm()
    return render(request, "reset_password.html", {"form": form})
