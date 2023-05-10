from django.shortcuts import render

from applipizza.models import Pizza, Ingredient, Composition
from applipizza.forms import IngredientForm, PizzaForm

# Create your views here.
def pizzas(request) :
    lesPizzas = Pizza.objects.all()
    return render(request, "applipizza/pizzas.html", {"pizzas" : lesPizzas } )

def ingredients(request) :
    lesIngredients = Ingredient.objects.all()
    return render(request, "applipizza/ingredients.html", {"ingredients" : lesIngredients })

def pizza(request, pizza_id):
    laPizza = Pizza.objects.get(idPizza = pizza_id)
    compo = Composition.objects.filter(pizza = pizza_id)
    return render(request, "applipizza/pizza.html",{"pizza" : laPizza,"composition" : compo})

def formulaireCreationIngredient(request):
    formulaire = IngredientForm()
    return render(request,"applipizza/formulaireCreationIngredient.html",{"form" : formulaire})

def creerIngredient(request):
    form = IngredientForm(request.POST)
    if form.is_valid() :
        nomIng = form.cleaned_data['nomIngredient']
        ing = Ingredient()
        ing.nomIngredient = nomIng
        ing.save()
        return render(request,"applipizza/traitementFormulaireCreationIngredient.html",{"nom" : nomIng})

def formulaireCreationPizza(request):
    formulaire = PizzaForm()
    return render(request,"applipizza/formulaireCreationPizza.html",{"form" : formulaire})

def creerPizza(request):
    form = PizzaForm(request.POST)
    if form.is_valid() :
        nomPiz = form.cleaned_data['nomPizza']
        prixPiz = form.cleaned_data['prix']
        piz = Pizza()
        piz.nomPizza = nomPiz
        piz.prix = prixPiz
        piz.save()
        return render(request,"applipizza/traitementFormulaireCreationPizza.html",{"nom" : nomPiz})

