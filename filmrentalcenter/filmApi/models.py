from django.db import models

# Create your models here.


class filmsModel(models.Model):
    GENRE_CHOICES = (
        ('fiction','Fiction'),
        ('action','Action'),
        ('drama','Drama'),
        ('crime','Crime'),
        ('comedy','Comedy')
    )
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=60,choices=GENRE_CHOICES)
    rentalfee = models.IntegerField()

    def __str__(self):
        return self.title