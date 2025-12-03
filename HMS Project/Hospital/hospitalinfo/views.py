from django.shortcuts import render, redirect
from .models import *
from .forms import *


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
    hospital = Hospital.objects.get(pk=hospital_id)
    if request.method == "POST":
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'update_hospital.html', {'form': form})


def delete_hospital(request, hospital_id):
    hospital = Hospital.objects.get(pk=hospital_id)
    hospital.delete()
    return redirect('hospitalinfo:hospital_list')


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
    doctor = Doctor.objects.get(pk=doctor_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'update_doctor.html', {'form': form})


def delete_doctor(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    doctor.delete()
    return redirect('hospitalinfo:doctor_list')


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
    depart = Department.objects.get(pk=depart_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=depart)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:depart_list')
    else:
        form = DepartmentForm(instance=depart)
    return render(request, 'update_depart.html', {'form': form})


def delete_depart(request, depart_id):
    depart = Department.objects.get(pk=depart_id)
    depart.delete()
    return redirect('hospitalinfo:depart_list')


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})


def add_appointment(request):
    if request.method == "POST":
        patient_name = request.POST.get("patient_name")

        patient = Patient.objects.filter(name__iexact=patient_name).first()
        if patient is None:
            patient = Patient.objects.create(
                name=patient_name,
                gender="Other",
                dob="2000-01-01",
                email="temp@example.com",
                phone="0000000000",
                address="Auto-created from appointment",
            )

        Appointment.objects.create(
            patient=patient,
            doctor_id=request.POST.get("doctor"),
            appointmentdate=request.POST.get("appointmentdate"),
            status=request.POST.get("status"),
            notes=request.POST.get("notes"),
        )
        return redirect("hospitalinfo:appointment_list")
    else:
        form = AppointmentForm()
    return render(request, "add_appointment.html", {"form": form})


def update_appointment(request, appointment_id):

    appointment = Appointment.objects.get(pk=appointment_id)  

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:appointment_list')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'update_appointment.html', {
        'form': form,
        'appointment': appointment
    })

def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    appointment.delete()
    return redirect('hospitalinfo:appointment_list')


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:patient_list')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})


def update_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'update_patient.html', {'form': form})


def delete_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    patient.delete()
    return redirect('hospitalinfo:patient_list')


def specialist_list(request):
    specialists = Specialist.objects.all()
    return render(request, 'specialist_list.html', {'specialists': specialists})


def add_specialist(request):
    if request.method == 'POST':
        form = SpecialistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:specialist_list')
    else:
        form = SpecialistForm()
    return render(request, 'add_specialist.html', {'form': form})


def update_specialist(request, specialist_id):
    specialist = Specialist.objects.get(pk=specialist_id)
    if request.method == 'POST':
        form = SpecialistForm(request.POST, instance=specialist)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:specialist_list')
    else:
        form = SpecialistForm(instance=specialist)
    return render(request, 'update_specialist.html', {'form': form})


def delete_specialist(request, specialist_id):
    specialist = Specialist.objects.get(pk=specialist_id)
    specialist.delete()
    return redirect('hospitalinfo:specialist_list')


def doctorSpecialty_list(request):
    doctorspecialtys = Doctorspecialty.objects.all()
    return render(request, 'doctorspecialty_list.html', {'doctorspecialtys': doctorspecialtys})


def add_doctorspecialty(request):
    if request.method == 'POST':
        form = DoctorSpecialtyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:doctorspecialty_list')
    else:
        form = DoctorSpecialtyForm()
    return render(request, 'add_doctorspecialty.html', {'form': form})


def update_doctorspecialty(request, doctorspecialty_id):
    doctorspecialty = Doctorspecialty.objects.get(pk=doctorspecialty_id)
    if request.method == 'POST':
        form = DoctorSpecialtyForm(request.POST, instance=doctorspecialty)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:doctorspecialty_list')
    else:
        form = DoctorSpecialtyForm(instance=doctorspecialty)
    return render(request, 'update_doctorspecialty.html', {'form': form})


def delete_doctorspecialty(request, doctorspecialty_id):
    doctorspecialty = Doctorspecialty.objects.get(pk=doctorspecialty_id)
    doctorspecialty.delete()
    return redirect('hospitalinfo:doctorspecialty_list')
