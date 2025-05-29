from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

def index(request):
    pokemon = ["Pikachu", "Charmander","Squartle", "Bulbasor"]
    template = loader.get_template("index.html")
    return HttpResponse (template.render({
        "pokemons": pokemons
    }, request))

def pokemon_details(request, pokemon):
    template = loader.get_template("pokemon_details.html")
    return HttpResponse(template.render({"pokemon":pokemon}, request))
