from rest_framework import routers

from src.cars_details.api.views.cars_details import CarsDetailsView

cars_details_api_router = routers.DefaultRouter()

cars_details_api_router.register("cars", CarsDetailsView)
