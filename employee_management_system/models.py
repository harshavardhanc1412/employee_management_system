from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length= 100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=100)
    #hno = models.Charfield(max_length=100)
    #street = models.CharField(max_length=50)
    #city = models.CharField(max_length=50)
    #state = models.CharField(max_length=50)

    #Work_exp = models.JSONField(default=list)
    #qualifications = models.JSONField(default=list)
    #projects = models.JSONField(default=list)

def __str__(self):
    return self.name

