# coding: utf-8

from boisson import Boisson


class CondimentDecorateur(Boisson):
    """Classe représentant un condiment abstrait décorateur qui peut être
    ajouté à n'importe quel Boisson.
    Il référence une Boisson pour utiliser la *composition*
    Il hérite de Boisson pour respecter l'interface de Boisson.
    """

    def __init__(self, sur_boisson):
        self.boisson = sur_boisson

    def description(self):
        return " + {description_boisson}" \
            .format(description_boisson=self.boisson.description)
