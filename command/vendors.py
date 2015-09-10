# coding: utf-8

"""
Objects/lib API that knows how to handle a request.
"""

class Light:

    def lights_on(self):
        print("** Lights : ON")

    def lights_off(self):
        print("** Lights: OFF")


class GarageDoor:

    def open_door(self):
        print("** Garage door: OPEN")

    def close_door(self):
        print("** Garage door: CLOSED")
