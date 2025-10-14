from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from .forms import *
from django.contrib import messages


# Registration
def signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, '🎉 Registration successful! You can now log in.')
            return redirect('HospitalLogin:login')
            
    else:
        form=signupForm()
    return render(request,'signup.html',{'form': form})

def login(request):
    if request.method=='POST':
        form=loginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data['username']
            psw=form.cleaned_data['password']
            user=authenticate(username=u_name,password=psw)

            if user is not None:
                return redirect('hospitalinfo:home')
            else:
                form.add_error(None,"Invalid username and password")
        
    else:
        form=loginForm()
    return render(request,'login.html',{'form': form})

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                messages.success(request, 'Password updated successfully. You can login now.')
                return redirect('HospitalLogin:login')
            except User.DoesNotExist:
                form.add_error('username', 'Username does not exist.')

    else:
        form = ResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form})







