from .language import api_router as define_language
from .tonality import api_router as define_tonality

list_of_routes = [
    define_tonality,
    define_language,
]


__all__ = [
    "list_of_routes",
]
