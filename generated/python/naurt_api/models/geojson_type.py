from enum import Enum

class GeojsonType(str, Enum):
    GEOJSON = "geojson"
    KEY_VALUE = "key_value"

    def __str__(self) -> str:
        return str(self.value)
