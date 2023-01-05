from functools import lru_cache

from enum import Enum


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
