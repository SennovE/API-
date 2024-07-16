from pydantic import BaseModel, Field


class Tonality(BaseModel):
    polarity: float = Field(ge=-1, le=1)
    subjectivity: float = Field(ge=0, le=1)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "polarity": 0.55544,
                    "subjectivity": 0.60568,
                }
            ]
        }
    }
