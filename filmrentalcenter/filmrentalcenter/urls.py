from django.urls import path,include
from rest_framework import routers

from customerApi import views
from filmApi import views as filmview
from rentalApi import views as rentalview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .customAPIs import customAPIs
router = routers.DefaultRouter()
router.register(r'customers',views.CustomerViewSet)
router.register(r'films',filmview.FilmViewSet)
router.register(r'rental',rentalview.RentalViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('customer-movies-rented/<int:customer_id>/', customAPIs.as_view(), name='customer-movies-rented'),
    path('movies-by-genre/<str:genre>/', customAPIs.as_view(), name='movies-by-genre'),
]
