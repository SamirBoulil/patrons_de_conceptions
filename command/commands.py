# coding: utf-8

from abc import ABCMeta
from abc import abstractmethod


class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute_on(self):
        return NotImplemented

    @abstractmethod
    def execute_off(self):
        return NotImplemented


class LightCommand(Command):
    """ Lights command

    :param light: reference to a light handler to open close door.
    :type light: `Vendor.Light`
    """

    def __init__(self, light_lib_handler):
        self.light = light_lib_handler

    def execute_on(self):
        self.light.lights_on()

    def execute_off(self):
        self.light.lights_off()

    def __str__(self):
        return "Lights command"

    def __repr__(self):
        return self.__str__()


class GarageDoorCommand(Command):
    """ Garage door command.

    :param garage_door: reference to a garage handler to open close door.
    :type garage: `Vendor.GarageDoor`
    """

    def __init__(self, garage_door_handler):
        self.garage_door = garage_door_handler

    def execute_on(self):
        self.garage_door.open_door()

    def execute_off(self):
        self.garage_door.close_door()

    def __str__(self):
        return "Garage door command"

    def __repr__(self):
        return self.__str__()


class NoCommand(Command):
    """ The No command command does nothing.
    just avoids to test for null in the remote so it's convenient.
    """

    def execute_on(self):
        print("** No command: Does nothing. Button not programmed yet.")

    def execute_off(self):
        print("** No command: Does nothing. Button not programmed yet.")

    def __str__(self):
        return "No command"

    def __repr__(self):
        return self.__str__()
