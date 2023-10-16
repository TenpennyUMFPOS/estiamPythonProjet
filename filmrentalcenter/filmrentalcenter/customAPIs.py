

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from customerApi.models import customersModel
from filmApi.models import filmsModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

class customAPIs(APIView):
    
    def get_movies_by_genre(self, request, genre):
        movies = filmsModel.objects.filter(genre=genre)
        movie_list = [movie.title for movie in movies]
        response_data = {
            "genre": genre,
            "movies_by_genre": movie_list,
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def get_movies_rented_by_customer(self, request, customer_id):
        customer = get_object_or_404(customersModel, id=customer_id)
        rental_count = customer.rentalrecordmodel_set.count()
        response_data = {
            "customer_id": customer.id,
            "customer_name": f"{customer.username}",
            "movies_rented": rental_count,
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def get(self, request, customer_id=None, genre=None):
        if genre:
            return self.get_movies_by_genre(request, genre)
        else:
            return self.get_movies_rented_by_customer(request, customer_id)
