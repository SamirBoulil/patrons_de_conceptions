# coding: utf-8


"""
Implementation of the command design pattern : Encapsulate requests in objects.

a remote control that can has inputs to send On actions and Off actions.
It has 10 of each and they are able to control Lights or GarageDoor.

Command pattern: Encapsulates a request as an object, thereby letting you
parametize clients with diffrents requests, queue or log requests, and support
undoable operations.
"""


from vendors import Light
from vendors import GarageDoor

from commands import LightCommand
from commands import GarageDoorCommand

from remote import Remote


def main():
    """ A remote control that is programmed to control the light in button 0
    and the garage door in the button 6
    """

    print("Initialization of the remote")
    remote = Remote()
    print(remote)

    # Programming button 1 to control lights
    light = Light()
    light_command = LightCommand(light)
    remote.set_command(0, light_command)
    print(remote)

    # Programming button 1 to control garage door
    garage_door = GarageDoor()
    garage_command = GarageDoorCommand(garage_door)
    remote.set_command(6, garage_command)
    print(remote)

    print("Testing possible actions")
    remote.press_on(0)
    remote.press_off(0)
    remote.press_on(6)
    remote.press_off(6)
    remote.press_on(1)
    remote.press_off(1)


if __name__ == "__main__":
    main()
