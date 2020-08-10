from enum import Enum

SIZE_SCALE_FACTOR = 1024


class FileSize:
    def __init__(self, size: int):
        self.size = size

    def __eq__(self, other):
        if type(other) is not FileSize:
            return False
        return self.size == other.size

    def __str__(self):

        unit = SizeUnit.of(self.size)
        value = self.size / unit.value

        if SizeUnit.Bytes.value < self.size < SizeUnit.Undefined.value:
            return f"{value:.2f} {unit.name}"
        elif 0 <= self.size <= 1:
            return f"{self.size} Byte"
        else:
            return SizeUnit.Undefined.name


class SizeUnit(Enum):
    Bytes = SIZE_SCALE_FACTOR ** 0
    KB = SIZE_SCALE_FACTOR ** 1
    MB = SIZE_SCALE_FACTOR ** 2
    GB = SIZE_SCALE_FACTOR ** 3
    TB = SIZE_SCALE_FACTOR ** 4
    PB = SIZE_SCALE_FACTOR ** 5
    EB = SIZE_SCALE_FACTOR ** 6
    ZB = SIZE_SCALE_FACTOR ** 7
    Undefined = SIZE_SCALE_FACTOR ** 8

    @staticmethod
    def of(raw_size) -> Enum:
        for unit in SizeUnit:
            if raw_size < unit.value * SIZE_SCALE_FACTOR:
                return unit

        return SizeUnit.Undefined
