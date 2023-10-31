import os
from enum import Enum

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    prod = "prod"
    dev = "dev"


class BaseAppSettings(BaseSettings):
    env_type: str = "dev"

    @property
    def app_env(self) -> AppEnvTypes:
        load_dotenv()

        env_type = os.environ.get("ENV_TYPE")
        match env_type:
            case "dev":
                return AppEnvTypes.dev
            case "prod":
                return AppEnvTypes.prod
            case _:
                return AppEnvTypes.dev

    class Config:
        env_file = ".env"
