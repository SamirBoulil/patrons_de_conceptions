# coding: utf-8

"""
Abstraction d'une pizza et les différents type concrêts de pizzas.
"""


class Pizza:
    """ Classe abstraite d'une pizza.

    :param nom: la nom de la pizza.
    """
    nom = ""

    def preparer(self):
        print ("... Preparer ...")

    def cuire(self):
        print ("... Cuisson ...")

    def decouper(self):
        print("... Découper ...")

    def mettre_en_carton(self):
        print("... Mise en carton ...")

    def __str__(self):
        return "Ma {nom} est prête!".format(nom=self.nom)


class PizzaVegetarienne(Pizza):

    def __init__(self):
        self.nom = "Pizza vegetarienne"


class PizzaFromage(Pizza):

    def __init__(self):
        self.nom = "Pizza aux trois fromages"
