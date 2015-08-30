# coding: utf-8


""" Nos fabriques abstraites dont l'objectif est de mettre à dispositions tous
les ingrédients nécessaires à la confection d'une pizza (création de sauce,
 de pate etc.).

En centralisant les méthodes de créations dans une classe, on se laisse la
possibilité de générer des types d'ingrédients ensemble.
"""


from ingredients import PateFine
from ingredients import PateEpaisse
from ingredients import SauceTomate
from ingredients import SauceFlamekuche
from ingredients import Champignons
from ingredients import Jambon
from ingredients import Lardons
from ingredients import Oignons


class PizzaIngredientFactory(object):

    name = None

    def creerPate(self):
        raise NotImplementedError()

    def creerSauce(self):
        raise NotImplementedError()

    def creerFromage(self):
        raise NotImplementedError()

    def creerIngredients(self):
        raise NotImplementedError()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Fournisseur officiel de la région {fournisseur}" \
            .format(fournisseur=self.name)


class NycPizzaIngregientFactory(PizzaIngredientFactory):
    """ Des pizzas qui ressemblent à la pizza reine. """

    def __init__(self):
        self.name = "New York City"

    def creerPate(self):
        return PateFine()

    def creerSauce(self):
        return SauceTomate()

    def creerIngredientsVegetarienne(self):
        return [Champignons()]

    def creerIngredientsReine(self):
        return [Jambon(), Champignons(), Oignons()]

    def creerIngredientsCalzone(self):
        return [Champignons(), Oignons()]  # oeufs


class ParisPizzaIngredientFactory(PizzaIngredientFactory):
    """ Des pizzas qui ressemblent à une pizza flamekuche.
    """

    def __init__(self):
        self.name = "Paris"

    def creerPate(self):
        return PateEpaisse()

    def creerSauce(self):
        return SauceFlamekuche()

    def creerIngredientsVegetarienne(self):
        return [Champignons()]

    def creerIngredientsReine(self):
        return [Jambon(), Oignons(), Lardons()]

    def creerIngredientsCalzone(self):
        return [Oignons()]
