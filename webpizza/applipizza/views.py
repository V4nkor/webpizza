from django.shortcuts import render

from applipizza.models import Pizza, Ingredient, Composition
from applipizza.forms import IngredientForm, PizzaForm, CompositionForm

# Create your views here.
def accueil(request):
    return render(request, "applipizza/accueil.html")

def pizzas(request) :
    lesPizzas = Pizza.objects.all()
    return render(request, "applipizza/pizzas.html", {"pizzas" : lesPizzas } )

def ingredients(request) :
    lesIngredients = Ingredient.objects.all()
    return render(request, "applipizza/ingredients.html", {"ingredients" : lesIngredients })

def pizza(request, pizza_id):
    formulaire = CompositionForm()
    laPizza = Pizza.objects.get(idPizza = pizza_id)
    compo = Composition.objects.filter(pizza = pizza_id)
    listeIngredients = []
    for c in compo :
        ing = Ingredient.objects.get(idIngredient = c.ingredient.idIngredient)
        listeIngredients.append({"nom" : ing.nomIngredient, "qte" : c.quantite})
    return render(request, "applipizza/pizza.html",{"pizza" : laPizza,"liste" : listeIngredients,"composition" : compo,"form" : formulaire})

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

def ajouterIngredientDansPizza(request,pizza_id):
    formulaire = CompositionForm(request.POST)
    if formulaire.is_valid():
        idIng = formulaire.cleaned_data['ingredient']
        qte = formulaire.cleaned_data['quantite']

        compo = Composition()
        compo.ingredient = Ingredient.objects.get(idIngredient = idIng)
        compo.pizza = Pizza.objects.get(idPizza = pizza_id)
        compo.quantite = qte
        compo.save()

    formulaire = CompositionForm()

    laPizza = Pizza.objects.get(idPizza = pizza_id)

    compo = Composition.objects.filter(pizza = pizza_id)

    listeIngredients = []

    for c in compo:
        ing = Ingredient.objects.get(idIngredient = c.ingredient.idIngredient)
        listeIngredients.append({"nom" : ing.nomIngredient, "qte" : c.quantite})

    return render(request,"applipizza/pizza.html",{"pizza" : laPizza,"liste" : listeIngredients,"form" : formulaire})

def supprimerPizza(request, pizza_id):
    pizza = Pizza.objects.get(idPizza = pizza_id)
    pizza.delete()
    lesPizzas = Pizza.objects.all()
    return render(request, "applipizza/pizzas.html", {"pizzas" : lesPizzas })

def afficherFormulaireModificationPizza(request,pizza_id):
    laPizza = Pizza.objects.get(idPizza = pizza_id)
    formulaire = PizzaForm(instance = laPizza)
    return render(request,"applipizza/formulaireModificationPizza.html",{"form" : formulaire,"pizza" : laPizza})

def modifierPizza(request, pizza_id):
    laPizza = Pizza.objects.get(idPizza = pizza_id)
    formulaire = PizzaForm(request.POST)
    if formulaire.is_valid():
        laPizza.nomPizza = formulaire.cleaned_data['nomPizza']
        laPizza.prix = formulaire.cleaned_data['prix']
        laPizza.save()
    laPizza = Pizza.objects.get(idPizza = pizza_id)
    return render(request,"applipizza/traitementFormulaireModificationpizza.html",{"pizza" : laPizza})

def supprimerIngredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(idIngredient = ingredient_id)
    ingredient.delete()
    lesIngredients = Ingredient.objects.all()
    return render(request, "applipizza/ingredients.html", {"ingredients" : lesIngredients })

def afficherFormulaireModificationIngredient(request,ingredient_id):
    leIngredient = Ingredient.objects.get(idIngredient = ingredient_id)
    formulaire = IngredientForm(instance = leIngredient)
    return render(request,"applipizza/formulaireModificationIngredient.html",{"form" : formulaire,"ingredient" : leIngredient})

def modifierIngredient(request, ingredient_id):
    leIngredient = Ingredient.objects.get(idIngredient = ingredient_id)
    formulaire = IngredientForm(request.POST)
    if formulaire.is_valid():
        leIngredient.nomIngredient = formulaire.cleaned_data['nomIngredient']
        leIngredient.save()
    leIngredient = Ingredient.objects.get(idIngredient = ingredient_id)
    return render(request,"applipizza/traitementFormulaireModificationingredient.html",{"ingredient" : leIngredient})