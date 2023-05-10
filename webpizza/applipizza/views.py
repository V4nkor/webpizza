from django.shortcuts import render

from applipizza.models import Pizza
from applipizza.models import Ingredient
from applipizza.models import Composition

# Create your views here.
def pizzas(request) :
    lesPizzas = Pizza.objects.all()
    return render(request,
    "applipizza/pizzas.html",
    {"pizzas" : lesPizzas }
    )

def ingredients(request) :
    lesIngredients = Ingredient.objects.all()
    return render(request,
    "applipizza/ingredients.html",
    {"ingredients" : lesIngredients }
    )

def pizza(request, pizza_id):
    laPizza = Pizza.objects.get(idPizza = pizza_id)
    compo = Composition.objects.filter(pizza = pizza_id)
    return render(request, "applipizza/pizza.html",{"pizza" : laPizza,"composition" : compo})