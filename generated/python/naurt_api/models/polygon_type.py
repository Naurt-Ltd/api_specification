from enum import Enum

class PolygonType(str, Enum):
    POLYGON = "Polygon"

    def __str__(self) -> str:
        return str(self.value)
