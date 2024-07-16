from fastapi import FastAPI

from text_analyser.endpoints import list_of_routes


def bind_routes(application: FastAPI) -> None:
    """
    Adds all routes to the application
    """
    for route in list_of_routes:
        application.include_router(route)


def get_app() -> FastAPI:
    """
    Creates a microservice
    """
    description = "A microservice that allows you to analyze text."

    application = FastAPI(
        title="TextAnalyser",
        description=description,
    )
    bind_routes(application)
    return application


app = get_app()
