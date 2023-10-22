from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import filmsModel


class FilmsViewSetTests(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="adminTest",
            password="123456",
            email="admin@test.com"
        )
        self.client.force_authenticate(user=self.superuser)

        self.film_data = {
            'title': 'test title',
            'director': 'test director',
            'genre': 'comedy',
            'rentalfee': 10
        }

        self.test_film = filmsModel.objects.create(
            title=self.film_data['title'],
            director=self.film_data['director'],
            genre=self.film_data['genre'],
            rentalfee=self.film_data['rentalfee']
        )

    def test_list_films(self):
        response = self.client.get('/films/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


    def test_post_films(self):
        film_data = {
        'title': 'New Test Film',
        'director': 'Test Director',
        'genre': 'action',
        'rentalfee': 8
        }

        response = self.client.post('/films/', film_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(filmsModel.objects.last().title, film_data['title'])
        self.assertEqual(filmsModel.objects.last().director, film_data['director'])
        self.assertEqual(filmsModel.objects.last().genre, film_data['genre'])
        self.assertEqual(filmsModel.objects.last().rentalfee, film_data['rentalfee'])

    def test_partial_update_film(self):
        film_data = {
            'title': 'Updated Title',
        }

        film_id = self.test_film.id
        response = self.client.patch(f'/films/{film_id}/', film_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.test_film.refresh_from_db()
        self.assertEqual(self.test_film.title, film_data['title'])

       
