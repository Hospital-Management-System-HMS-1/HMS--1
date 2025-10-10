from django.shortcuts import render, redirect
from .forms import HospitalForm


# adding
def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'add_hospital.html', {'form': form})
