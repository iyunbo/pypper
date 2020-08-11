from enum import Enum

SIZE_SCALE_FACTOR = 1024
MINIMUM_SIZE = 0


class FileSize:
    def __init__(self, size: int):
        if Unit.Infinite.value >= size >= MINIMUM_SIZE:
            self.size = size
        else:
            raise ValueError(f"file size out of bounds [{MINIMUM_SIZE} - {Unit.Infinite.value}]: {size}")

    def __eq__(self, other):
        if type(other) is not FileSize:
            return False
        return self.size == other.size

    def __str__(self):

        unit = Unit.of(self.size)
        value = self.size / unit.value

        if Unit.Bytes.value < self.size < Unit.Infinite.value:
            return f"{value:.2f} {unit.name}"
        else:
            return f"{self.size} Byte"


class Unit(Enum):
    Bytes = SIZE_SCALE_FACTOR ** 0
    KB = SIZE_SCALE_FACTOR ** 1
    MB = SIZE_SCALE_FACTOR ** 2
    GB = SIZE_SCALE_FACTOR ** 3
    TB = SIZE_SCALE_FACTOR ** 4
    PB = SIZE_SCALE_FACTOR ** 5
    EB = SIZE_SCALE_FACTOR ** 6
    ZB = SIZE_SCALE_FACTOR ** 7
    Infinite = SIZE_SCALE_FACTOR ** 8

    @staticmethod
    def of(raw_size) -> Enum:
        for unit in Unit:
            if raw_size < unit.value * SIZE_SCALE_FACTOR:
                return unit
