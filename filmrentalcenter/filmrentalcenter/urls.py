from django.urls import path,include
from rest_framework import routers

from customerApi import views
from filmApi import views as filmview
from rentalApi import views as rentalview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="film rental center API",
        default_version="v1"
    ),
    public=True,
    

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
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]
