from fastapi import APIRouter, Query
from starlette import status

from text_analyser.utils import define_language, run_in_thread

api_router = APIRouter()


@api_router.get(
    "/api/v1/language",
    status_code=status.HTTP_200_OK,
    response_model=str,
)
async def define_language_of_the_text(
    text: str = Query(
        ...,
        description="Determines the language of the given text, better in usage with long texts",
    )
):
    tonalities = await run_in_thread(define_language, text)
    return tonalities
