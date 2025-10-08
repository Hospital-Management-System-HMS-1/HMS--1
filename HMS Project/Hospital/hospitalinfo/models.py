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
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments')
	name = models.CharField(max_length=100)
	description = models.Text()

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


