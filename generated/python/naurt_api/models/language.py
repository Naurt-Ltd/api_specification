from enum import Enum

class Language(str, Enum):
    AR = "AR"
    AUTO = "Auto"
    CZ = "CZ"
    DE = "DE"
    EN = "EN"
    FI = "FI"
    FR = "FR"
    IT = "IT"
    JA = "JA"
    KO = "KO"
    NL = "NL"
    NO = "NO"
    PL = "PL"
    PT = "PT"
    SL = "SL"
    ZH = "ZH"

    def __str__(self) -> str:
        return str(self.value)
