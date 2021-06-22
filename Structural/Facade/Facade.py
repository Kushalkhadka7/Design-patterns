from __future__ import annotations

from abc import ABC, abstractmethod


class IConverter(ABC):
    @abstractmethod
    def convert_video(self) -> None:
        pass


class Processor:
    def __init__(self, file):
        self._file = file

    def process_video(self):
        print(f"Processing video file {self._file}")


class Compressor:
    def __init__(self, file):
        self._file = file

    def compress_video(self):
        print(f"Compressing video file {self._file}")


class VideoConverter(IConverter):
    def __init__(self, file, video_format):
        self._file = file
        self._format = video_format

    def convert_video(self) -> str:
        Processor(self._file)
        Compressor(self._file)

        return f"Successfully converted video {self._file}"


video_converted = VideoConverter('video.mp4', "mpeg")
print(video_converted.convert_video())
