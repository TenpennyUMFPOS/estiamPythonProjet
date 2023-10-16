from rest_framework import serializers

from .models import rentalRecordModel

class RentalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rentalRecordModel
        fields =('customer','film','rentaldate','returndate')