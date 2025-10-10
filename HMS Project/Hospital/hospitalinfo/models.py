from django.db import models

# Model: Hospital
# This model stores general information about a hospital 

class Hospital(models.Model):
	hospital_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	address = models.TextField()
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=20)
	email = models.EmailField()
	website = models.URLField(blank=True, null=True)
	rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

# Model: Department
# Each hospital can have multiple departments (like Cardiology, Neurology, etc.)

class Department(models.Model):
	dept_id = models.AutoField(primary_key=True)
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments') #Thkis will redirect to the certain deptname for the 
	name = models.CharField(max_length=100)
	description = models.TextField()

#  Model: Doctor
#  Stores doctor details. Each doctor belongs to a hospital and a department.

class Doctor(models.Model):
	doctor_id = models.AutoField(primary_key=True)
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')
	dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='doctors')
	name = models.CharField(max_length=100)
	qualification = models.CharField(max_length=100)
	specialization = models.CharField(max_length=100)
	email = models.EmailField()
	availability = models.CharField(max_length=100)  # e.g. "Monday to Friday, 10am–1pm"
	rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

# Model: Patient


class Patient(models.Model):
	patient_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 25)
	dob = models.DateField()
	email = models.EmailField()
	password_hash = models.TextField()	
	phone = models.CharField(max_length=15)
	address = models.TextField()

# Models : Appointment
# Stores all the present and upcoming appoinments of all the doctors and patients 

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50)  # e.g. "Scheduled", "Completed", "Cancelled"
    notes = models.TextField()



class Patient(models.Model):
	patient_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 25)
	dob = models.DateField()
	email = models.EmailField()
	password_hash = models.TextField()	
	phone = models.CharField(max_length=15)
	address = models.TextField()
