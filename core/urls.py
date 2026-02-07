# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("leaf/", views.leaf_upload, name="leaf"),
    path("soil/", views.soil_recommendation, name="soil"),
]
