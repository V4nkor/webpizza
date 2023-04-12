from django.db import models

# Create your models here.
class Ingredient(models.Model) :
    idIngredient = models.AutoField(primary_key = True)

    nomIngredient = models.CharField(max_length = 50, verbose_name = 'le nom de l\'ingredient ')
    
    def __str__(self) -> str:
        return 'ingredient ' + self.nomIngredient

class Pizza(models.Model) :
    idPizza = models.AutoField(primary_key = True)

    nomPizza = models.CharField(max_length = 50, verbose_name = 'le nom de cette pizza ')

    prix = models.DecimalField(max_digits = 4, decimal_places = 2, verbose_name = 'le prix' )

    def __str__(self) -> str:
        return 'pizza' + self.nomPizza + ' (prix = ' + str(self.prix) + '$)'