# coding: utf-8


"""
We use an adapater class (object adaptater) to translate from the duck
interface (quack, fly) to the turkey interface (gobble, fly).
"""


class Duck:

    def quack(self):
        raise NotImplementedError()

    def fly(self):
        raise NotImplementedError()


class Turkey:

    def gobble(self):
        print("GLOUGLOU GLOUGLOU")

    def fly(self):
        print("Turkey flying")


class Turkey_adaptater(Duck):

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()
