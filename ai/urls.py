from django.urls import path
from . import views

urlpatterns = [
    path("health", views.health),
    path("monuments/<str:monument_id>", views.fiche),
]
