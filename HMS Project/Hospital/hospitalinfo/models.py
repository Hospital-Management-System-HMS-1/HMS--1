from django.db import models


class Hospital(models.Model):
    hospitalid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contactnumber = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    deptid = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctorid = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors")
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="doctors")
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()
    availability = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    patientid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=25)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    appointmentid = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    appointmentdate = models.DateTimeField()
    status = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return f"Appointment {self.appointmentid}"


class Specialist(models.Model):
    specialtyid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Doctorspecialty(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor.name} - {self.specialty.name}"
