# coding: utf-8

from canard import Canard
from vole_non import VoleNon
from queuk import Queuk


class Poule(Canard):

    def __init__(self):
        self.vole_comportement = VoleNon()
        self.quack_comportement = Queuk()
