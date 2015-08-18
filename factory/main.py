# coding: utf-8

"""Implémentation du patron de conception methode factory

Le but est de crééer et de préparer des pizzas de différents types
à l'aide d'une factory.
"""

from magasin_pizza import MagasinPizza


def main():
    print("Bienvenue dans mon Pizza Store")
    mon_magasin = MagasinPizza()

    print("Un client demande une pizza vegetarienne !")
    vegetarienne = mon_magasin.commander("vegetarienne")
    print(vegetarienne)

    print("Un client demande une pizza au fromage !")
    fromage = mon_magasin.commander("fromage")
    print(fromage)


if __name__ == "__main__":
    main()
