from django.urls import path, include
from . import views
from src.cars.api.router import cars_api_router

urlpatterns = [
    path("/", include(cars_api_router.urls)),
]
