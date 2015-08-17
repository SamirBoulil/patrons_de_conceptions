# coding: utf-8

from vole_comportement import VoleComportement


class VoleNon(VoleComportement):
    """ Des canards qui malheureusement ne volent pas """

    def vole(self):
        print("je ne vole pas. :'(")
