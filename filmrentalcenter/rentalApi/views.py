from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .models import rentalRecordModel
from .serializers import RentalSerializer

from customerApi.models import customersModel

class RentalViewSet(viewsets.ModelViewSet):
    queryset = rentalRecordModel.objects.all()
    serializer_class = RentalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data )
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = [{'id': record.id,'customer': record.customer.id, 'film': record.film.title,'rentaldate': record.rentaldate,'returndate': record.returndate,}for record in queryset] 
        return Response(data)
    
    

