from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from .config import get_app_settings
from .di import init_dependencies
from .routers import init_routers


def get_application() -> FastAPI:
    settings = get_app_settings()
    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    init_routers(application)
    init_dependencies(application)

    return application


app = get_application()
