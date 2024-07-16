from typing import Annotated

from fastapi import APIRouter, Body
from starlette import status

from text_analyser.schemas import SentenceWithTone, Tonality
from text_analyser.utils import (
    define_tonality,
    define_tonality_in_sentences,
    run_in_thread,
)

api_router = APIRouter()


@api_router.post(
    "/api/v1/text_tonality",
    status_code=status.HTTP_200_OK,
    response_model=Tonality,
)
async def define_text_tonality(
    text: Annotated[
        str, Body(embed=True, description="Determines the tone of the entire text.")
    ]
):
    tonalities = await run_in_thread(define_tonality, text)
    return tonalities


@api_router.post(
    "/api/v1/sentences_tonality",
    status_code=status.HTTP_200_OK,
    response_model=list[SentenceWithTone],
)
async def define_sentences_tonality(
    text: Annotated[
        str,
        Body(embed=True, description="Determines the tone of individual sentences."),
    ]
):
    tonalities = await run_in_thread(define_tonality_in_sentences, text)
    return tonalities
