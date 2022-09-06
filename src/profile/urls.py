from django.urls import path
from . import views
from src.profile.api.views.profile import RegisterView

urlpatterns = [path("_registration/", RegisterView.as_view(), name="registe")]
