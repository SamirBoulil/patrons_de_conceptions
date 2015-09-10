# coding: utf-8

""" Créons des magasins de notre franchise à différents endroits de la planètes.
Nos pizzas disponibles sont les suivantes :
        - Pizza végétarienne
        - Pizza reine
        - Pizza calzone

Nous avons trois restaurants situés :
        - NYC, USA
        - Paris, FRA
"""


from pizza_store_factory import NycStore
from pizza_store_factory import ParisStore


def main():
    # NYC - style
    nyc_store = NycStore()
    nyc_store.welcomeMessage()

    veggie_nyc = nyc_store.commanderPizza("vegetarienne")
    print(veggie_nyc)

    calzone_nyc = nyc_store.commanderPizza("calzone")
    print(calzone_nyc)

    reine_nyc = nyc_store.commanderPizza("reine")
    print(reine_nyc)

    # Paris - style
    paris_store = ParisStore()
    paris_store.welcomeMessage()

    veggie_paris = paris_store.commanderPizza("vegetarienne")
    print(veggie_paris)

    calzone_paris = paris_store.commanderPizza("calzone")
    print(calzone_paris)

    reine_paris = paris_store.commanderPizza("reine")
    print(reine_paris)


if __name__ == "__main__":
    main()