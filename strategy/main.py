# coding: utf-8

from col_vert import ColVert
from poule import Poule
from vole_ailes import VoleAiles
from queuk import Queuk


def main():
    """ Une bascoure, des poules et des canards
    """
    c1 = ColVert()
    c1.vole()
    c1.quack()

    poule = Poule()
    poule.vole()
    poule.quack()

    pouleMutante = Poule()
    pouleMutante.vole_comportement = VoleAiles()
    pouleMutante.vole()
    pouleMutante.quack_comportement = Queuk()
    pouleMutante.quack()


if __name__ == "__main__":
    main()