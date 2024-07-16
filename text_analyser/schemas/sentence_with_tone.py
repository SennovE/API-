from pydantic import BaseModel

from text_analyser.schemas.tonality import Tonality


class SentenceWithTone(BaseModel):
    sentence: str
    tonality: Tonality

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sentence": "You are so pretty!",
                    "tonality": {"polarity": 0.3125, "subjectivity": 1},
                }
            ]
        }
    }
