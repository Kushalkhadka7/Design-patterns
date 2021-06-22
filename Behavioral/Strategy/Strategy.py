from abc import ABC, abstractmethod


class IStrategy(ABC):

    @abstractmethod
    def execute_strategy(self):
        pass


class ByCycle(IStrategy):

    def execute_strategy(self):
        print(f'By cycle strategy is implemented')


class ByBus(IStrategy):

    def execute_strategy(self):
        print(f'By bus strategy is implemented')


class ByCar(IStrategy):

    def execute_strategy(self):
        print(f'By car strategy is implemented')


class Context:
    _strategy: IStrategy

    def set_strategy(self, strategy: IStrategy):
        self._strategy = strategy

    def execute(self):
        self._strategy.execute_strategy()


class Application:
    def main(self, strategy):
        context = Context()
        if strategy == 'bus':
            bus = ByBus()
        else:
            raise Exception("Strategy not found")
        context.set_strategy(bus)
        context.execute()


app = Application()
app.main('bus')
