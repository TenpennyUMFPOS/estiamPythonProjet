from django.urls import path,include
from rest_framework import routers

from customerApi import views
from filmApi import views as filmview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'customers',views.CustomerViewSet)
router.register(r'films',filmview.FilmViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]