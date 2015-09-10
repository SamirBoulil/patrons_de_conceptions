# coding: utf-8


from commands import NoCommand


class Remote:
    """
    A programmable remote control that can handle 10 on slots and 10 off slots.
    """

    COMMAND_NUMBER = 10

    def __init__(self):
        self.slots = [NoCommand() for i in range(0, Remote.COMMAND_NUMBER)]

    def set_command(self, index, command):
        self.slots[index] = command

    def press_on(self, index):
        self.slots[index].execute_on()

    def press_off(self, index):
        self.slots[index].execute_off()

    def __str__(self):
        state = "Remote state\n"
        for index, command in enumerate(self.slots):
            state += "#{index} - {command}\n".format(
                index=index, command=command
            )

        return state

    def __repr__(self):
        return self.__str__()
