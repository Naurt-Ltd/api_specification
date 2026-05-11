from enum import Enum

class FinalDestinationMatchLevel(str, Enum):
    POSTALCODE = "Postalcode"
    STREET = "Street"
    STREETNUMBER = "StreetNumber"
    UNIT = "Unit"

    def __str__(self) -> str:
        return str(self.value)
