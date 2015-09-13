# coding: utf-8


"""
What if our system which knows how to handles ducks and chicken, would like to
manage turkeys (which has totally diffrent interfaces.

They gobble instead of quacking.
They fly really wierdly (they need 5 fly for one duck fly).

Plus the Turkey implementation is not ours to decide. It is a read-only vendor
class.

Adaptateur pattern: Converts the interface of a class into another interface
the client expects. Adaptateur let's classes work together that couldn't
otherwise because of incompatible interfaces.
"""

from duck_to_turkey import Turkey
from duck_to_turkey import Turkey_adaptater


def main():
    turkey = Turkey()
    adapt_turkey = Turkey_adaptater(turkey)
    adapt_turkey.quack()
    adapt_turkey.fly()


if __name__ == "__main__":
    main()
