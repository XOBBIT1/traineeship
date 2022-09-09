from rest_framework import routers

from src.profile.api.views.profile import RegisterView

profile_api_router = routers.DefaultRouter()

profile_api_router.register("profile", RegisterView)
