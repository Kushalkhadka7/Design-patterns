from abc import ABC, abstractmethod
from typing import List


class IListener(ABC):

    @abstractmethod
    def update(self):
        pass


class IPublisher(ABC):
    listeners: IListener = []

    @abstractmethod
    def subscribe(self, listener: IListener):
        pass

    @abstractmethod
    def un_subscribe(self, listener: IListener):
        pass

    @abstractmethod
    def notify(self):
        pass


class Publisher(IPublisher):
    listeners: List[IListener] = []

    def subscribe(self, listener: IListener):
        self.listeners.append(listener)

    def un_subscribe(self, listener: IListener):
        self.listeners.pop(listener)

    def notify(self):
        for listener in self.listeners:
            listener.update()


class LoggingListener(IListener):

    def __init__(self, message):
        self.message = message

    def update(self):
        print(f"Logging {self.message}")


class EmailAlertListener(IListener):

    def __init__(self, message):
        self.message = message

    def update(self):
        print(f"Sending email {self.message}")


class EditorEvent:
    publisher: IPublisher

    def __init__(self):
        self.publisher = Publisher()

    def open_file(self):
        self.publisher.notify()


editor = EditorEvent()
logger = LoggingListener("hello")
email = EmailAlertListener("hello")

editor.publisher.subscribe(logger)
editor.publisher.subscribe(email)


editor.open_file()
