"""Component Enums shared by models and schemas"""

from enum import Enum as E

class AcquisitionType(E):
    """Enum value for building acquisition method"""
    CONSTRUCTION = "construction"
    GRANT = "grant"
    LEASE = "lease"
    PURCHASE = "purchase"
    OTHER = "other"

    @classmethod
    def validate(cls, s):
        valid_types = { e.value for e in cls }
        if not isinstance(s, str) or s.lower not in valid_types:
            raise ValueError(f"No type match for string \"{s}\"")
        return s.lower()
