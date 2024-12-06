from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    # specialization = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    # contact = models.CharField(max_length=15, blank=True, null=True)  # New contact field
    # appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='appointments', blank=True,
    #                                 null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient =models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.patient.name+"--"+self.doctor.name

    # mobile = models.CharField(null=True, max_length=10)
    # gender = models.CharField(max_length=10)
    # address = models.CharField(max_length=100)

