from django import forms
from .models import *

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'   # include all fields from the model

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
        
        
