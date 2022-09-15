from . import views
from src.provider.api.router import provider_api_router
from django.urls import path, include

urlpatterns = [
    path("/", include(provider_api_router.urls)),
]
