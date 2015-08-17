# coding: utf-8

from vole_comportement import VoleComportement


class VoleAiles(VoleComportement):
    """Un canard qui vole avec les ailes"""

    def vole(self):
        print("je vole avec mes ailes, très haut et très loin !!")
