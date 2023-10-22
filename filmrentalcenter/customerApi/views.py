from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import customersModel
from .serializers import CustomersSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = customersModel.objects.all()
    serializer_class = CustomersSerializer
     


    @swagger_auto_schema(
    operation_description="Create a customer",
    responses={201: openapi.Response('Customer created', CustomersSerializer)},
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'exampleTest': openapi.Schema(
                type=openapi.TYPE_STRING,
                description='Example description',
                ),
            },
        required=['exampleTest'],
        )
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data )
        serializer.is_valid(raise_exception = True)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = [{'id': customer.id, 'username': customer.username, 'email': customer.email, 'password': customer.password,'role': customer.role} for customer in queryset]
        return Response(data)
    
    @swagger_auto_schema(
        operation_description="List customers",
        responses={200: openapi.Response('List of customers', CustomersSerializer(many=True))},
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginated_queryset = self.paginate_queryset(queryset)  
        serializer = self.get_serializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Update a customer",
        responses={200: openapi.Response('Customer updated', CustomersSerializer)},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'exampleTest': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Example description',
                ),
            },
            required=['exampleTest'],
        )
    )
    def partial_update(self, request, *args, **kwargs):
        customerId = kwargs.get('pk')
        customer = get_object_or_404(customersModel, pk=customerId)

        serialiser = self.get_serializer(customer,data= request.data, partial = True)
        serialiser.is_valid(raise_exception = True)
        self.perform_update(serialiser)
        return  Response(serialiser.data)
    @swagger_auto_schema(
        operation_description="Delete a customer",
        responses={200: openapi.Response('Customer deleted', CustomersSerializer)},
    )
    def destroy(self, request, *args, **kwargs):
        customerId = kwargs.get('pk')
        customer = get_object_or_404(customersModel, pk=customerId)
        customer.delete()
        return Response("User Was deleted successfully")
    
    
    

