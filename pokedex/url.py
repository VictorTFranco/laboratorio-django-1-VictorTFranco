from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:pokemon>/", views.pokemon_details, name="pokemon_details")
]
