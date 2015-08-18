# coding: utf-8

from pizza_factory import PizzaFactory


class MagasinPizza:
    """ Un magasin de pizza qui pérapre des pizzas peu importe le type

    Il se fournit en pizza à l'aide d'une factory qui se charge de
    l'instanciation de la bonne pizza en fonction de ce que le client demande.

    :param fournisseur_pizza: Factory à la quelle est déléguée l'instanciation.
    """

    def __init__(self):
        self.fournisseur_pizza = PizzaFactory()
        super(MagasinPizza, self).__init__()

    def commander(self, type_pizza):
        pizza = self.fournisseur_pizza.obtenir(type_pizza)

        pizza.preparer()
        pizza.cuire()
        pizza.decouper()
        pizza.mettre_en_carton()

        return pizza
