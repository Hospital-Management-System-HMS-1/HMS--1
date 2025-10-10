from django.shortcuts import render, redirect
from .forms import HospitalForm
from .models import *


# adding
def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospitalinfo:hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'add_hospital.html', {'form': form})


#hosipal list
def hospital_list(request):
    hospital_L=Hospital.objects.all()
    return render(request,'hospital_list.html',{'hospitals': hospital_L})

def delete_hospital(request,hospital_id):
    hospital=Hospital.objects.get(pk=hospital_id)
    hospital.delete()
    return redirect('hospitalinfo:hospital_list')
