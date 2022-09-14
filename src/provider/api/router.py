from rest_framework import routers

from src.provider.api.views.provider import ProviderView

provider_api_router = routers.DefaultRouter()

provider_api_router.register("provider", ProviderView)
