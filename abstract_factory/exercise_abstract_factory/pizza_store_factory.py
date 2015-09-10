# coding: utf-8

"""
Nos implémentations de magasin.
"""


from pizza_ingredients_factory import NycPizzaIngregientFactory
from pizza_ingredients_factory import ParisPizzaIngredientFactory

from pizzas import Vegetarienne
from pizzas import Reine
from pizzas import Calzone


class PizzaStore:

    name = None

    def commanderPizza(self, pizza_type):
        print(" * (" + self.name + ") Ordering pizza : " + pizza_type)
        pizza = self.creerPizza(pizza_type)

        pizza.preparer()
        pizza.enfourner()
        pizza.couper()
        pizza.mettre_en_boite()

        return pizza

    def welcomeMessage(self):
        print("-"*50)
        print("Bienvenue à PIZZA dot {name}".format(name=self.name))
        print("-"*50)

    def creerPizza(self, pizza_type):
        ingredient_factory = self.creerIngredientFactory()

        if pizza_type == "vegetarienne":
            return Vegetarienne(ingredient_factory)
        elif pizza_type == "reine":
            return Reine(ingredient_factory)
        elif pizza_type == "calzone":
            return Calzone(ingredient_factory)
        else:
            raise ValueError("Unsupported pizza type")

    def creerIngredientFactory(self):
        raise NotImplementedError()


class NycStore(PizzaStore):

    name = "NYC"

    def creerIngredientFactory(self):
        return NycPizzaIngregientFactory()


class ParisStore(PizzaStore):

    name = "Paris"

    def creerIngredientFactory(self):
        return ParisPizzaIngredientFactory()
