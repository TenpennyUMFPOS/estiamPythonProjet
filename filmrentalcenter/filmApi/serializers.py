from rest_framework import serializers

from .models import filmsModel

class FilmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = filmsModel
        fields = ('title','director','genre','rentalfee')

