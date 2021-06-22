from __future__ import annotations


class Logger:
    _instances = {}
    _logs = []

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def debug(self, message) -> None:
        self._logs.append(message)
        print(f"[DEBUG]: {message}")

    def get_logs(self):
        return self._logs


class FirstImplementation:
    _logger: Logger

    def __init__(self) -> None:
        self._logger = Logger()

    def display_message(self) -> None:
        self._logger.debug("First implementations")


class SecondImplementation:
    _logger: Logger

    def __init__(self) -> None:
        self._logger = Logger()

    def display_message(self) -> None:
        self._logger.debug("Second implementations")


firstImplementation = FirstImplementation()
firstImplementation.display_message()

secondImplementation = SecondImplementation()
secondImplementation.display_message()


logger = Logger()
print(logger.get_logs())
