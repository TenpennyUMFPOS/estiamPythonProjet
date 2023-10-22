from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


# Create your views here.

from .models import filmsModel
from .serializers import FilmsSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class FilmViewSet(viewsets.ModelViewSet):
    queryset = filmsModel.objects.all()
    serializer_class = FilmsSerializer
    throttle_classes = [UserRateThrottle]
    filter_backends = [filters.SearchFilter] 
    #permission_classes = [IsAuthenticated] activate this to use token
    search_fields = ['title', 'director', 'genre']

    
 
    @swagger_auto_schema(
        operation_description="Create a film",
        responses={201: openapi.Response('Film created', FilmsSerializer)},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the film'),
                'director': openapi.Schema(type=openapi.TYPE_STRING, description='Director of the film'),
                'genre': openapi.Schema(type=openapi.TYPE_STRING, description='Genre of the film'),
                'rentalfee': openapi.Schema(type=openapi.TYPE_INTEGER, description='Rental fee of the film'),
            },
            required=['title', 'director', 'genre', 'rentalfee']
        )
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data )
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    #def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = [{'id': film.id, 'title': film.title, 'director': film.director, 'genre': film.genre,'rental fee': film.rentalfee} for film in queryset]
        return Response(data)
    
    @swagger_auto_schema(
        operation_description="List films",
        responses={200: openapi.Response('List of films', FilmsSerializer(many=True))}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginated_queryset = self.paginate_queryset(queryset)  

        serializer = self.get_serializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_description="Partial update a film",
        responses={200: openapi.Response('Film updated', FilmsSerializer)},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the film'),
                'director': openapi.Schema(type=openapi.TYPE_STRING, description='Director of the film'),
                'genre': openapi.Schema(type=openapi.TYPE_STRING, description='Genre of the film'),
                'rentalfee': openapi.Schema(type=openapi.TYPE_INTEGER, description='Rental fee of the film'),
            }
        )
    )
    def partial_update(self, request, *args, **kwargs):
        filmId = kwargs.get('pk')
        film = get_object_or_404(filmsModel,pk=filmId)

        serializer = self.get_serializer(film,data = request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Delete a film",
        responses={200: openapi.Response('Film deleted')}
    ) 
    def destroy(self, request, *args, **kwargs):
        filmId = kwargs.get('pk')
        film = get_object_or_404(filmsModel,pk=filmId)
        film.delete()
        return Response("Film was deleted successfully")

    