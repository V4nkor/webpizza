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

class Composition(models.Model) :
    class Meta :
        unique_together = ('ingredient','pizza')
    idComposition = models.AutoField(primary_key = True)

    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)

    quantite = models.CharField(max_length = 100, verbose_name = 'la quantite ')

    def __str__(self) -> str:
        ing = self.ingredient
        piz = self.pizza
        return ing.__str__() + ' fait partie de la pizza ' + piz.__str__() + ' (auqntite = '+ self.quantite +')'