# coding: utf-8


""" Liste des ingrédients nécessaires à la préparation d'une pizza.
Une pate (fine ou epaisse), une sauce (ici tomate ou crême fraîche) et des
ingrédients par dessus.

Ce sont les produits de nos fabriques abstraites.
"""


class Pate(object):
    name = None

    def __repr__(self):
        return "Pate : {name}".format(name=self.name)

    def __str__(self):
        return self.__repr__()


class PateFine(Pate):

    def __init__(self):
        self.name = "Fine"


class PateEpaisse(Pate):

    def __init__(self):
        self.name = "Double"


class Sauce(object):
    name = None

    def __repr__(self):
        return "Sauce : {name}".format(name=self.name)

    def __str__(self):
        return self.__repr__()


class SauceTomate(Sauce):

    def __init__(self):
        self.name = "Tomate"


class SauceFlamekuche(Sauce):

    def __init__(self):
        self.name = "Blanche Flamekuche"


class Ingredient(object):
    name = None

    def __repr__(self):
        return "Ingredient : {name}".format(name=self.name)

    def __str__(self):
        return self.__repr__()


class Champignons(Ingredient):

    def __init__(self):
        self.name = "Champignon"


class Lardons(Ingredient):

    def __init__(self):
        self.name = "Lardons"


class Jambon(Ingredient):

    def __init__(self):
        self.name = "Jambon blanc"


class Oignons(Ingredient):

    def __init__(self):
        self.name = "Oignons"
