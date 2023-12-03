from django.urls import path

from .views import LocationAPI

urlpatterns = [
    path('office/', LocationAPI.as_view(), name='office'),
]
