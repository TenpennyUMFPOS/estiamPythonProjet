from django.db import models
from customerApi.models import customersModel
from filmApi.models import filmsModel
# Create your models here.

class rentalRecordModel(models.Model):
    customer = models.ForeignKey(customersModel, on_delete= models.CASCADE)
    film = models.ForeignKey(filmsModel,on_delete= models.CASCADE)
    rentaldate = models.DateField()
    returndate = models.DateField()


    def __str__(self):
         return f"Rental Record for {self.customer.first_name} {self.customer.last_name} - Film: {self.film.title}"
