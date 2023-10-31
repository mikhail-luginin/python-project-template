from fastapi import FastAPI

from .controllers.root import root_router
from .healthcheck import healthcheck_router


def init_routers(app: FastAPI) -> None:
    app.include_router(root_router, prefix="/api")
    app.include_router(healthcheck_router)
