from django.urls import path

from .views import LocationAPI, VehicleAPI

urlpatterns = [
    path('office/', LocationAPI.as_view(), name='office'),
    path('get/', VehicleAPI.as_view(), name='vehicle'),
]
