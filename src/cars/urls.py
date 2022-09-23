from src.cars.api.router import cars_api_router
from src.cars.api.views.cars import SalonByeCarsView, ProfileByeCarsView
from django.urls import path, include
from . import views

urlpatterns = [
    path("/", include(cars_api_router.urls)),
    path("_buy_salon/<int:pk>/", SalonByeCarsView.as_view(), name="bye_salon"),
    path("_buy_profile/<int:pk>/", ProfileByeCarsView.as_view(), name="bye_profile"),
]
