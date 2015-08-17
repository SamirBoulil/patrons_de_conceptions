# coding: utf-8

from canard import Canard
from vole_ailes import VoleAiles
from quick import Quick


class ColVert(Canard):

    def __init__(self):
        self.vole_comportement = VoleAiles()
        self.quack_comportement = Quick()
