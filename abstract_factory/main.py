# coding: utf-8

from pizza_ingredients_factory import AllemagnePizzaIngredientFactory
from pizza_ingredients_factory import NYCPizzaIngregientFactory


def main():
    """ Different pizza store locations
    delivering different versions of the same pizzas.
    """
    Allemagne_pif = AllemagnePizzaIngredientFactory()
    print(Allemagne_pif)
    print(Allemagne_pif.creerPate())
    print(Allemagne_pif.creerSauce())
    print(Allemagne_pif.creerIngredients())

    print("-"*50)

    NYC_pif = NYCPizzaIngregientFactory()
    print(NYC_pif)
    print(NYC_pif.creerPate())
    print(NYC_pif.creerSauce())
    print(NYC_pif.creerIngredients())


if __name__ == "__main__":
    main()
