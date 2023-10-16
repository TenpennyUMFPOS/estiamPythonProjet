from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .models import filmsModel
from .serializers import FilmsSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = filmsModel.objects.all()
    serializer_class = FilmsSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data )
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = [{'id': film.id, 'title': film.title, 'director': film.director, 'genre': film.genre,'rental fee': film.rentalfee} for film in queryset]
        return Response(data)
    
    def partial_update(self, request, *args, **kwargs):
        filmId = kwargs.get('pk')
        film = get_object_or_404(filmsModel,pk=filmId)

        serializer = self.get_serializer(film,data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        filmId = kwargs.get('pk')
        film = get_object_or_404(filmsModel,pk=filmId)
        film.delete()
        return Response("Film was deleted successfully")