from enum import Enum

class FeaturePropertiesNaurtType(str, Enum):
    BASIC_GEOCODE = "basic_geocode"
    NAURT_BUILDING = "naurt_building"
    NAURT_DOOR = "naurt_door"
    NAURT_PARKING = "naurt_parking"

    def __str__(self) -> str:
        return str(self.value)
