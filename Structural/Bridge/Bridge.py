from __future__ import annotations
from abc import ABCMeta, abstractmethod


class RemoteControl:
    device: Device

    def __init__(self, device: Device) -> None:
        self.device = device

    def toggle_power(self) -> None:
        if self.device.isEnabled:
            self.device.disable()
        else:
            self.device.enable()


class AdvanceRemoteControl(RemoteControl):
    def mute() -> None:
        self.device.setVolume(0)


class Device(metaclass=ABCMeta):
    isEnabled = False

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass


class Television(Device):

    isEnabled = False

    def disable(self) -> None:
        print("disabled")

    def enable(self) -> None:
        print("enabled")


device = Television()
remote = RemoteControl(device)

remote.toggle_power()
