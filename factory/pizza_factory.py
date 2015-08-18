# coding: utf-8

from pizzas import PizzaVegetarienne
from pizzas import PizzaFromage


class PizzaFactory(object):

    def obtenir(self, type_pizza):
        """Implémentation du patron méthode factory.

        la fonction obtenir esr responsable de l'instanciation de la bonne pizza
        en fonction de la valeur passée en paramètre.

        :param type_pizza: le type de pizza à instancier
        """
        pizza = None
        if type_pizza == "vegetarienne":
            pizza = PizzaVegetarienne()
        elif type_pizza == "fromage":
            pizza = PizzaFromage()
        else:
            raise NotImplementedError

        return pizza
