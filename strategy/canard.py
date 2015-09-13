# coding: utf-8


from quack_comportement import Queuk
from quack_comportement import Quick

from vole_comportement import VoleAiles
from vole_comportement import VoleNon


class Canard(object):
    """Un cannard peut faire quack, voler et nager."""

    vole_comportement = None
    quack_comportement = None

    def vole(self):
        """Methode abstraite pour effectuer un vol"""
        self.vole_comportement.vole()

    def quack(self):
        """Méthode abstraite pour faire un "Quaaack"""
        self.quack_comportement.quack()

    def nage(self):
        """Un canard sait nager"""
        print("Je nage...")


class ColVert(Canard):

    def __init__(self):
        self.vole_comportement = VoleAiles()
        self.quack_comportement = Quick()


class Poule(Canard):

    def __init__(self):
        self.vole_comportement = VoleNon()
        self.quack_comportement = Queuk()
