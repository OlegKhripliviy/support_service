from enum import Enum
from functools import lru_cache


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    MANAGER = "manager"

    @classmethod
    @lru_cache
    def values(cls) -> list[tuple[str, str]]:
        results = []
        for element in cls:
            el = (element.value, element.value.capitalize())
            results.append(el)
        return results
