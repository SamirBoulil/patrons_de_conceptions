# coding: utf-8


class Boisson(object):
    """Interface générique représentant une boisson (chaude ou froide).
    """

    description = "Boisson inconnue"

    def prix(self):
        """ Retourne le prix de la boisson
        :returns: le prix de la boisson
        """
        raise NotImplementedError


class CafeNoir(Boisson):
    """Un cafe noir bien chaud
    """

    def __init__(self):
        self.description = "Cafe noir"

    def prix(self):
        return 1.5
