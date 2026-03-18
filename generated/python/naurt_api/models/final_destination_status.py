from enum import Enum

class FinalDestinationStatus(str, Enum):
    NO_MATCHES = "no_matches"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
