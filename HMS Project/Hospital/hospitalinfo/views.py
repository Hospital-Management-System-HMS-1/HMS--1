from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# ---------------- HOSPITAL ----------------
def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})

def add_hospital(request):
    if request.method == "POST":
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'add_hospital.html', {'form': form})

def update_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    if request.method == "POST":
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'update_hospital.html', {'form': form})

def delete_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    hospital.delete()
    return redirect('hospitalinfo:hospital_list')


# ---------------- DOCTOR ----------------
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})

def update_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'update_doctor.html', {'form': form})

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    doctor.delete()
    return redirect('hospitalinfo:doctor_list')


# ---------------- DEPARTMENT ----------------
def depart_list(request):
    departments = Department.objects.all()
    return render(request, 'depart_list.html', {'departments': departments})

def add_depart(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:depart_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_depart.html', {'form': form})

def update_depart(request, depart_id):
    depart = get_object_or_404(Department, pk=depart_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=depart)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:depart_list')
    else:
        form = DepartmentForm(instance=depart)
    return render(request, 'update_depart.html', {'form': form})

def delete_depart(request, depart_id):
    depart = get_object_or_404(Department, pk=depart_id)
    depart.delete()
    return redirect('hospitalinfo:depart_list')


# ---------------- APPOINTMENT ----------------
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'add_appointment.html', {'form': form})

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'update_appointment.html', {'form': form})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    return redirect('hospitalinfo:appointment_list')
