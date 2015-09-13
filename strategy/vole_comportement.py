# coding: utf-8


"""
Strategies for flying.
"""


class VoleComportement(object):
    """ Interface décrivant les méthodes pour qu'un canard puisse voler.
    """

    def vole(self):
        """ Les vols concrêts doivent implémenter.
        """
        raise NotImplementedError()


class VoleAiles(VoleComportement):
    """Un canard qui vole avec les ailes"""

    def vole(self):
        print("je vole avec mes ailes, très haut et très loin !!")


class VoleNon(VoleComportement):
    """ Des canards qui malheureusement ne volent pas """

    def vole(self):
        print("je ne vole pas. :'(")
