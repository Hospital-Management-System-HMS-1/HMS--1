from django.shortcuts import render, redirect, get_object_or_404
from .forms import HospitalForm, DepartmentForm, DoctorForm, AppointmentForm
from .models import Hospital, Department, Doctor, Appointment

def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'hospitalinfo/add_hospital.html', {'form': form})

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospitalinfo/hospital_list.html', {'hospitals': hospitals})

def update_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'hospitalinfo/update_hospital.html', {'form': form})

def delete_hospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)
    hospital.delete()
    return redirect('hospitalinfo:hospital_list')

# ------------------- Department Views -------------------
def depart_list(request):
    departments = Department.objects.all()
    return render(request, 'hospitalinfo/depart_list.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:depart_list')
    else:
        form = DepartmentForm()
    return render(request, 'hospitalinfo/add_depart.html', {'form': form})

def update_depart(request, dept_id):
    depart = get_object_or_404(Department, pk=dept_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=depart)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:depart_list')
    else:
        form = DepartmentForm(instance=depart)
    return render(request, 'hospitalinfo/update_depart.html', {'form': form})

def delete_depart(request, dept_id):
    depart = get_object_or_404(Department, pk=dept_id)
    depart.delete()
    return redirect('hospitalinfo:depart_list')

# ------------------- Doctor Views -------------------
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospitalinfo/doctor_list.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'hospitalinfo/add_doctor.html', {'form': form})

def update_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'hospitalinfo/update_doctor.html', {'form': form})

def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    doctor.delete()
    return redirect('hospitalinfo:doctor_list')

# ------------------- Appointment Views -------------------
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospitalinfo/appointment_list.html', {'appointments': appointments})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'hospitalinfo/add_appointment.html', {'form': form})

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'hospitalinfo/update_appointment.html', {'form': form})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    return redirect('hospitalinfo:appointment_list')
