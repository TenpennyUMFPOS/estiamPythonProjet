from django.db import models

# Create your models here.


class customersModel(models.Model):
    ROLE_CHOICES = (
        ('customer','Customer'),
        ('admin','Admin'),
    )

    username = models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10,choices= ROLE_CHOICES)


    def __str__(self):
        return self.username