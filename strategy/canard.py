# coding: utf-8


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
