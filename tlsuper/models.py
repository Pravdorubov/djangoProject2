from django.db import models

# Create your models here.
class Duty(models.Model):
    name = models.CharField(max_length=200)

class Employer(models.Model):
    name = models.CharField(max_length=200)
    date_employment = models.DateTimeField()
    salary = models.IntegerField()
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE())

