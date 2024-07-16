from iso639 import Lang
from langdetect import detect


def define_language(text: str) -> str:
    code = detect(text)
    language = Lang(code)
    if language:
        return language.name
    else:
        return "Unknown"
