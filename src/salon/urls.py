from django.urls import path, include
from . import views
from src.salon.api.router import salon_api_router
from src.salon.api.views.salon import (
    BuyView,
)

urlpatterns = [
    path("/", include(salon_api_router.urls)),
    path("_buy_car", BuyView.as_view(), name="buy"),
]
