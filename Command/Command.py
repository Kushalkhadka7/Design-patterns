from abc import ABC, abstractmethod


class Command(ABC):
    value = 0
    history = []

    @abstractmethod
    def execute(self, command):
        pass

    @abstractmethod
    def undo(self):
        pass


class Calculator(Command):
    value = 0
    history = []

    def execute(self, command):
        self.value = command.execute(self.value)
        self.history.append(command)

    def undo(self):
        command = self.history.pop()
        self.value = command.undo()


class AddCommand:
    value = 0
    added_value = 0

    def __init__(self, value):
        self.value = value
        self.added_value = value

    def execute(self, current_value):
        self.added_value = current_value
        return self.value + current_value

    def undo(self):
        return self.value - self.added_value


add_command = AddCommand(10)
print(add_command.execute(20))
print(add_command.undo())
