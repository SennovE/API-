import re

from textblob import TextBlob

from text_analyser.schemas import SentenceWithTone, Tonality


def define_tonality(text: str) -> Tonality:
    text_info = TextBlob(text)
    return Tonality(
        polarity=round(text_info.sentiment.polarity, 5),
        subjectivity=round(text_info.sentiment.subjectivity, 5),
    )


def define_tonality_in_sentences(text: str) -> list[SentenceWithTone]:
    text_info = TextBlob(text)
    tonalities = [
        SentenceWithTone(sentence=part, tonality=define_tonality(part))
        for part in re.split(r"[.!?]", text)
        if part.strip()
    ]
    return tonalities
