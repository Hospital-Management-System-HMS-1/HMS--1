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


