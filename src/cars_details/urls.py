from . import views
from src.cars_details.api.router import cars_details_api_router
from django.urls import path, include

urlpatterns = [
    path("/", include(cars_details_api_router.urls)),
]
