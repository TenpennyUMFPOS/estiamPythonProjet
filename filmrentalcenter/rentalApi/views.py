from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .models import rentalRecordModel
from .serializers import RentalSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from customerApi.models import customersModel

class RentalViewSet(viewsets.ModelViewSet):
    queryset = rentalRecordModel.objects.all()
    serializer_class = RentalSerializer


    @swagger_auto_schema(
        operation_description="Create a rental record",
        responses={201: openapi.Response('Rental record created', RentalSerializer)},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'customer': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the customer'),
                'film': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the film'),
                'rentaldate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Rental date'),
                'returndate': openapi.Schema(type=openapi.TYPE_STRING, format='date', description='Return date'),
            },
            required=['customer', 'film', 'rentaldate', 'returndate']
        )
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data )
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    #def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = [{'id': record.id,'customer': record.customer.id, 'film': record.film.title,'rentaldate': record.rentaldate,'returndate': record.returndate,}for record in queryset] 
        return Response(data) 
    
    @swagger_auto_schema(
        operation_description="List rental records",
        responses={200: openapi.Response('List of rental records', RentalSerializer(many=True))}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginated_queryset = self.paginate_queryset(queryset)  
        serializer = self.get_serializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Delete a rental record",
        responses={200: openapi.Response('Rental record deleted')}
    )
    def destroy(self, request, *args, **kwargs):
        recordId = kwargs.get('pk')
        record = get_object_or_404(rentalRecordModel,pk=recordId)
        record.delete()
        return Response("Rental records was deleted successfully")
    

