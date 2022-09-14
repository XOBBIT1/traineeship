from src.cars.api.views.cars import CarsView
from rest_framework import routers

cars_api_router = routers.DefaultRouter()

cars_api_router.register("cars", CarsView)
