from django import forms
from .models import Hospital, Department, Doctor, Appointment, Patient, Specialist, Doctorspecialty


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = "__all__"


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    STATUS_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
        ("Pending", "Pending"),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES)
    appointmentdate = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = Appointment
        # patient is set in the view, not via the form
        fields = ["doctor", "appointmentdate", "status", "notes"]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class SpecialistForm(forms.ModelForm):
    class Meta:
        model = Specialist
        fields = "__all__"


class DoctorSpecialtyForm(forms.ModelForm):
    class Meta:
        model = Doctorspecialty
        fields = "__all__"
