from rest_framework import routers

from src.cars.api.views.cars import CarsView

cars_api_router = routers.DefaultRouter()

cars_api_router.register('cars', CarsView)