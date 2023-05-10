from django import forms
from django.forms import ModelForm
from applipizza.models import Ingredient, Pizza

class IngredientForm(ModelForm) :
    class Meta :
        model = Ingredient
        fields = ['nomIngredient']


#class IngredientForm(forms.Form) :
#    nomIngredient = forms.CharField(
#            label = 'Nom de cet ingredient',
#            max_length = 50
#        )

class PizzaForm(ModelForm) :
    class Meta :
        model = Pizza
        fields = ['nomPizza','prix']


#classPizzaForm(forms.Form) :
#    nomPizza = forms.CharField(
#            label = 'Nom de cet ingredient',
#            max_length = 50
#        )
#    prix = forms.DecimalField()(
#            label = 'Prix de cet ingredient',
#        )
