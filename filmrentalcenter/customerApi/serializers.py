from rest_framework import serializers

from .models import customersModel


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= customersModel
        fields = ('username','email','password','role')