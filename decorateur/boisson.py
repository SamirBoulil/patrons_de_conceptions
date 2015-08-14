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
