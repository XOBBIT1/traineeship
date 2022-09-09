from rest_framework import routers

from src.salon.api.views.salon import SalonView

salon_api_router = routers.DefaultRouter()

salon_api_router.register("salon", SalonView)
