from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import customersModel
from .serializers import CustomersSerializer
from .views import CustomerViewSet

class CustomersModelTest(TestCase):
    def test_customer_creation(self):
        customer = customersModel.objects.create(
            username="testuser",
            email="test@example.com",
            password="test123",
            role="customer"
        )
        self.assertEqual(customer.username, "testuser")
        self.assertEqual(customer.email, "test@example.com")
        self.assertEqual(customer.password, "test123")
        self.assertEqual(customer.role, "customer")

class CustomerViewSetTests(APITestCase):
    def test_create_customer(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "test123",
            "role": "customer"
        }

        response = self.client.post('/customers/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(customersModel.objects.count(), 1)
        self.assertEqual(customersModel.objects.get().username, "testuser")

    def test_list_customers(self):
        response = self.client.get('/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


    def test_update_customer(self):
        
        customer = customersModel.objects.create(username="testuser", email="test@example.com", password="test123", role="customer")

        data = {
            "username": "updateduser",
            "email": "updated@example.com",
            "password": "newpass",
            "role": "admin"
        }

        response = self.client.patch(f'/customers/{customer.id}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        customer.refresh_from_db()
        self.assertEqual(customer.username, "updateduser")
        self.assertEqual(customer.email, "updated@example.com")
        self.assertEqual(customer.password, "newpass")
        self.assertEqual(customer.role, "admin")

    def test_delete_customer(self):
        
        customer = customersModel.objects.create(username="testuser", email="test@example.com", password="test123", role="customer")

        response = self.client.delete(f'/customers/{customer.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(customersModel.objects.count(), 0)