from __future__ import annotations

from abc import ABC


class IDataSource(ABC):
    _file: str = None

    def read_data(self) -> str:
        pass

    def write_data(self, data: str) -> None:
        pass


class FileDataSource(IDataSource):
    def __init__(self, file: str) -> None:
        self._file = file

    def read_data(self) -> None:
        print(f"Reading data from ${self._file}")

    def write_data(self, data: str) -> None:
        print(f"Writing to the file ${self._file}")


class Compressor(IDataSource):
    _wrappedContent: IDataSource = None

    def __init__(self, wrapped_content):
        self._wrappedContent = wrapped_content

    def read_data(self) -> str:
        print(f"Decompressing the data from {self._wrappedContent._file}")
        return f"Decompressing the data from {self._wrappedContent._file}"

    def write_data(self, data: str) -> None:
        print(f"Compressing the file {self._wrappedContent._file}")


class Application:
    @staticmethod
    def configure():
        source = FileDataSource('data.txt')
        source.write_data("Hello world")
        source.read_data()

        decorator = Compressor(source)

        decorator.write_data("Hello world")
        decorator.read_data()


Application.configure()
