from rest_framework import routers

from src.cars.api.views.cars import CarsView, SalonByeCarsView

cars_api_router = routers.DefaultRouter()
cars_api_salon_router = routers.SimpleRouter()

cars_api_router.register("cars", CarsView)
cars_api_salon_router.register("cars_salon", SalonByeCarsView)