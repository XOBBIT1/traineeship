from . import views
from src.profile.api.views.profile import RegisterView
from django.urls import path, include
from src.profile.api.router import profile_api_router

urlpatterns = [
    path("/", include(profile_api_router.urls)),
]
