# coding: utf-8

from boisson import CafeNoir
from condiment_decorateur import Chantilly


"""
Decorator pattern: The decorator pattern attaches additionnal responsibilities
to an object dynamically. Decorators provide flexible alternative to subclassing
for extending functionnality.
"""


def main():
    """ Implémentation du patron de conception décorateur
    Des cafés et des condiments.
    """
    my_cafe = CafeNoir()
    my_cafe_chantilly = Chantilly(CafeNoir())

    print("prix de mon cafe : {prix}".format(prix=str(my_cafe.prix())))
    print("prix de mon cafe chantilly : {prix}"
          .format(prix=str(my_cafe_chantilly.prix())))


if __name__ == "__main__":
    main()
