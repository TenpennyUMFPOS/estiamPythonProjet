from customerApi.models import customersModel
from filmApi.models import filmsModel

 
    

def get_movies_by_genre(fgenre):
    try:
        movies = filmsModel.objects.get(genre=fgenre)
        return movies
    except filmsModel.DoesNotExist:
        return 0