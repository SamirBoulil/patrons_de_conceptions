# coding: utf-8

from condiment_decorateur import CondimentDecorateur


class Chantilly(CondimentDecorateur):
    """ Une boule de chantilly par dessus hummmm...
    """

    description = "Chantilly"

    def prix(self):
        return .99 + self.boisson.prix()
