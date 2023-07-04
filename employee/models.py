from django.db import models
from manager.models import CustomUser
from django.urls import reverse


class Employee(models.Model):
    phon_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    position = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='employees')
    

    def get_absolute_url(self):
        return reverse('home')
    

class Penalty(models.Model):   
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='penalties')
    fee = models.PositiveIntegerField() 






