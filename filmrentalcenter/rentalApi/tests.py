from rest_framework import status
from rest_framework.test import APITestCase
from .models import rentalRecordModel  
from .serializers import RentalSerializer  
from customerApi.models import customersModel
from filmApi.models import filmsModel

class RentalRecordModelTests(APITestCase):
    def setUp(self):
        self.customer = customersModel.objects.create(username="testuser", email="test@example.com", password="test123", role="customer")
        self.film = filmsModel.objects.create(title="Test Film", director="Test Director", genre="action", rentalfee=8)

    def test_create_rental_record(self):
        data = {
        "customer": f"/customers/{self.customer.id}/",
        "film": f"/films/{self.film.id}/",
        "rentaldate": "2023-09-09",
        "returndate": "2023-09-16"
        }

        response = self.client.post('/rental/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_rental_records(self):
        # Create a rental record
        rentalRecordModel.objects.create(customer=self.customer, film=self.film, rentaldate="2023-09-01", returndate="2023-09-15")

        response = self.client.get('/rental/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_rental_record(self):
        # Create a rental record
        rental_record = rentalRecordModel.objects.create(customer=self.customer, film=self.film, rentaldate="2023-09-01", returndate="2023-09-15")

        response = self.client.delete(f'/rental/{rental_record.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
