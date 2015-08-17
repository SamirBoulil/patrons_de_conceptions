# coding: utf-8


class VoleComportement(object):
    """ Interface décrivant les méthodes pour qu'un canard puisse voler.
    """

    def vole(self):
        """ Les vols concrêts doivent implémenter.
        """
        raise NotImplementedError()
