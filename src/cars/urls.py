from . import views
from src.cars.api.router import cars_api_router
from django.urls import path, include


urlpatterns = [
    path("/", include(cars_api_router.urls)),
]
