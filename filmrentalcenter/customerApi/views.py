from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .models import customersModel
from .serializers import CustomersSerializer
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = customersModel.objects.all()
    serializer_class = CustomersSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data )
        serializer.is_valid(raise_exception = True)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = [{'id': customer.id, 'username': customer.username, 'email': customer.email, 'password': customer.password,'role': customer.role} for customer in queryset]
        return Response(data)
    
    def partial_update(self, request, *args, **kwargs):
        customerId = kwargs.get('pk')
        customer = get_object_or_404(customersModel, pk=customerId)

        serialiser = self.get_serializer(customer,data= request.data, partial = True)
        serialiser.is_valid(raise_exception = True)
        self.perform_update(serialiser)
        return  Response(serialiser.data)
    
    def destroy(self, request, *args, **kwargs):
        customerId = kwargs.get('pk')
        customer = get_object_or_404(customersModel, pk=customerId)
        customer.delete()
        return Response("User Was deleted successfully")
    
    
