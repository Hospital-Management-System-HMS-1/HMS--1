from django.shortcuts import render, redirect
from .forms import *
from .models import *

def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'add_hospital.html', {'form': form})


def hospital_list(request):
    hospital_L=Hospital.objects.all()
    return render(request,'hospital_list.html',{'hospitals': hospital_L})

def update_hospital(request,hospital_id):
    hospital=Hospital.objects.get(pk=hospital_id)
    if request.method=='POST':
        form=HospitalForm(request.POST,instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form=HospitalForm(instance=hospital)
    return render(request,'update_hospital.html',{'form': form})


#delete hospital
def delete_hospital(request,hospital_id):
    hospital=Hospital.objects.get(pk=hospital_id)
    hospital.delete()

    return redirect('hospitalinfo:hospital_list')

# Department views
# Create (Add Department)
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:depart_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_depart.html', {'form': form})

def depart_list(request):
    departments = Department.objects.all()
    return render(request, 'depart_list.html', {'departments': departments})


def update_depart(request,dept_id):
    depart=Department.objects.get(pk=dept_id)
    if request.method=='POST':
        form=DepartmentForm(request.POST,instance=depart)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:depart_list')
    else:
        form=DepartmentForm(instance=depart)
    return render(request,'update_depart.html',{'form': form})

def delete_depart(request,dept_id):
    depart=Department.objects.get(pk=dept_id)
    depart.delete()
    return redirect('hospitalinfo:depart_list')


def update_hospital(request, hospital_id):
    hospital = Hospital.objects.get(pk=hospital_id)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'update_hospital.html', {'form': form})



def doctor_list(request):
    doctor = doctor.objects.all()
    return render(request)

def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:doctor_list') 
    else:
        form = DoctorForm()
    return render(request,'add_doctor.html',{'form':form})