from django.db import models

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

class Department(models.Model):
	dept_id = models.AutoField(primary_key=True)
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments')  
	name = models.CharField(max_length=100)
	description = models.TextField()

class Doctor(models.Model):
	doctor_id = models.AutoField(primary_key=True)
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')
	dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='doctors')
	name = models.CharField(max_length=100)
	qualification = models.CharField(max_length=100)
	specialization = models.CharField(max_length=100)
	email = models.EmailField()
	availability = models.CharField(max_length=100)
	rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

class Patient(models.Model):
	patient_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 25)
	dob = models.DateField()
	email = models.EmailField()
	password_hash = models.TextField()	
	phone = models.CharField(max_length=15)
	address = models.TextField()

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    notes = models.TextField()

class Specialty(models.Model):
	specialty_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)

class DoctorSpecialty(models.Model):
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	specialty = models.ForeignKey(Specialty,on_delete=models.CASCADE)
<<<<<<< HEAD

=======
>>>>>>> 30982e75f4c9f975552e0f07d6aab6228eaa6b44
