"""carshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("src.salon.urls")),
    path("profile", include("src.profile.urls")),
    path("cars", include("src.cars.urls")),
    path("salon", include("src.salon.urls")),
    path("provider", include("src.provider.urls")),
    path("cars_details", include("src.cars_details.urls")),
    path("profile", include("django.contrib.auth.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)