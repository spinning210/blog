from django.urls import path
from . import views

urlpatterns = [
    path('covid19_world_map', views.covid19_world_map, name = "covid19_world_map"),
]