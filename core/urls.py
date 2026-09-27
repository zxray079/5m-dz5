"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('session-auth/', include('rest_framework.urls')),

    path('drf-auth-token/', obtain_auth_token, name='api_auth'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('task/', include('apps.serial.urls')),
    path('product/', include('apps.product.urls')),
    path('mixin/', include('apps.mixin.urls')),
    path('zones/', include('apps.zones.urls')),
]