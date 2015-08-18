# coding: utf-8

from boisson import Boisson


class CafeNoir(Boisson):
    """Un cafe noir bien chaud
    """

    def __init__(self):
        self.description = "Cafe noir"

    def prix(self):
        return 1.5
