from django.urls import path, include
from . import views
from src.cars_details.api.router import cars_details_api_router

urlpatterns = [
    path('/', include(cars_details_api_router.urls)),
]