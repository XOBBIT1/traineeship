from django.urls import path, include
from . import views
from src.profile.api.views.profile import (
    VerfyEmail,
    LoginView,
    LogoutView,
    RegisterView,
    BuyView,
)
from src.profile.api.router import profile_api_router

urlpatterns = [
    path("/", include(profile_api_router.urls)),
    path("_email", VerfyEmail.as_view(), name="email"),
    path("_login", LoginView.as_view(), name="login"),
    path("_logout", LogoutView.as_view(), name="logout"),
    path("_buy_car", BuyView.as_view(), name="buy"),
]
