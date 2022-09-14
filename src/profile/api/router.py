from src.profile.api.views.profile import RegisterView
from rest_framework import routers

profile_api_router = routers.DefaultRouter()

profile_api_router.register("profile", RegisterView)
