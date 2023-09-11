import logging

from .app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev FastAPI example application"

    logging_level: int = logging.DEBUG
    
    db_user: str
    db_name: str
    db_password: str
    db_host: str
    db_port: str

    class Config(AppSettings.Config):
        env_file = "dev.env"
