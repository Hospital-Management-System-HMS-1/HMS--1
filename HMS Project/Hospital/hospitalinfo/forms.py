from django import forms
from .models import *

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'   

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'      

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'    

class SpecialistForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__' 

class DoctorSpecialtyForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'