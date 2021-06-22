from __future__ import annotations


class Target:
    def __init__(self) -> None:
        pass

    def request(self) -> str:
        return f"Default Behavior."


class Adapted:
    def __init__(self) -> None:
        pass

    def specific_request(self) -> str:
        return f"Behavior to adapt."


class Adaptor(Target):
    def __init__(self, adapted: Adapted) -> None:
        super(Adaptor, self).__init__()
        self.adapted = adapted

    def request(self) -> str:
        result = self.adapted.specific_request()

        return result


target = Target()
print(target.request())


adapted = Adapted()
print(adapted.specific_request())


adaptor = Adaptor(adapted)
print(adaptor.request())
