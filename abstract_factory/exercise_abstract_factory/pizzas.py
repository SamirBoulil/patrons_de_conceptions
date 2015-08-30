# coding: utf-8


""" Nos pizzas disponibles sont les suivantes :
        - Pizza végétarienne
        - Pizza reine
        - Pizza calzone

    Nous avons trois restaurants situés :
        - NYC, USA
        - Paris, FRA
"""


class Pizza(object):

    def __init__(self, ingredient_factory):
        self.name = None
        self.pate = None
        self.sauce = None
        self.ingredients = []
        self.ingredient_factory = ingredient_factory

    def preparer(self):
        raise NotImplementedError()

    def couper(self):
        print("Decoupage de la pizza")

    def enfourner(self):
        print("Fast baking 12 minuts")

    def mettre_en_boite(self):
        print("Mise en boite, Emballé c'est pesé")

    def __repr__(self):
        repre = "Pizza " + self.name + " prête ! \n"
        repre += "Pate : " + str(self.pate) + "\n"
        repre += "sauce : " + str(self.sauce) + "\n"
        repre += "Ingredients : " + str(self.ingredients) + "\n"
        return repre

    def __str__(self):
        return self.__repr__()


class Vegetarienne(Pizza):

    def __init__(self, igf):
        super(Vegetarienne, self).__init__(igf)
        self.name = "Vegetarienne"

    def preparer(self):
        self.pate = self.ingredient_factory.creerPate()
        self.sauce = self.ingredient_factory.creerSauce()
        self.ingredients = \
            self.ingredient_factory.creerIngredientsVegetarienne()


class Reine(Pizza):

    def __init__(self, igf):
        super(Reine, self).__init__(igf)
        self.name = "Reine"

    def preparer(self):
        self.pate = self.ingredient_factory.creerPate()
        self.sauce = self.ingredient_factory.creerSauce()
        self.ingredients = self.ingredient_factory.creerIngredientsReine()


class Calzone(Pizza):

    def __init__(self, igf):
        super(Calzone, self).__init__(igf)
        self.name = "Calzone"

    def preparer(self):
        self.pate = self.ingredient_factory.creerPate()
        self.sauce = self.ingredient_factory.creerSauce()
        self.ingredients = self.ingredient_factory.creerIngredientsCalzone()
