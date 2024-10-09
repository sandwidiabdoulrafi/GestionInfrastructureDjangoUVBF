"""
URL configuration for GestionInfrastructure project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

import AppGestionInfrastructure

# from AppGestionInfrastructure.views import AdministrationViewSet, CitoyenViewSet, inscriptionViewSet


# router.register('citoyen', CitoyenViewSet, basename='citoyen')
# router.register('administration', AdministrationViewSet, basename='administration')
# router.register('inscription', inscriptionViewSet, basename='inscription')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('infratructure/', include('AppGestionInfrastructure.urls'))
    # path('api/', include(router.urls)),
]