# coding: utf-8

"""
Strategies for quacking.
"""


class Quack(object):
    """ Interface quack"""

    def quack(self):
        """Méthode abstraite"""
        raise NotImplementedError()


class Queuk(Quack):

    def quack(self):
        print("queuuueuck")


class Quick(Quack):
    """Le comportement est quick"""

    def quack(self):
        print("Quiiiiiiiiiiick")
