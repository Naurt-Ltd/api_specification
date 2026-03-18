from enum import Enum

class InputFilter(str, Enum):
    LOOSE = "loose"
    NONE = "none"
    STRICT = "strict"

    def __str__(self) -> str:
        return str(self.value)
