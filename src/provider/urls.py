from django.urls import path, include
from . import views
from src.provider.api.router import provider_api_router

urlpatterns = [
    path("/", include(provider_api_router.urls)),
]
