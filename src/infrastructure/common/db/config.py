import os
from dataclasses import dataclass

from dotenv import load_dotenv

from . import exceptions


@dataclass
class DBConfig:
    DB_USER: str | None
    DB_PASSWORD: str | None
    DB_HOST: str | None
    DB_PORT: str | None
    DB_NAME: str | None
    
    def validate(self):
        if not self.DB_USER:
            raise exceptions.DBUserNotFound("Database user not found")
        if not self.DB_PASSWORD:
            raise exceptions.DBPasswordNotFound("Database password not found")
        if not self.DB_NAME:
            raise exceptions.DBNameNotFound("Database name not found")
        if not self.DB_HOST:
            raise exceptions.DBHostNotFound("Database host not found")
        if not self.DB_PORT:
            raise exceptions.DBPortNotFound("Database port not found")


def database_credentials() -> dict:
    load_dotenv(dotenv_path='dev.env')
    load_dotenv(dotenv_path='prod.env')
    db_config = DBConfig(
        DB_USER=os.environ.get("DB_USER"),
        DB_HOST=os.environ.get("DB_HOST"),
        DB_NAME=os.environ.get("DB_NAME"),
        DB_PASSWORD=os.environ.get("DB_PASSWORD"),
        DB_PORT=os.environ.get("DB_PORT")
    )
    db_config.validate()
    return {
        "connector": 'postgresql+psycopg2',
        "user": db_config.DB_USER,
        "password": db_config.DB_PASSWORD,
        "host": db_config.DB_HOST,
        "port": db_config.DB_PORT,
        "database": db_config.DB_NAME
    }
