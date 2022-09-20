from django.urls import path, include
from . import views
from src.salon.api.router import salon_api_router

urlpatterns = [
    path("/", include(salon_api_router.urls)),
]
