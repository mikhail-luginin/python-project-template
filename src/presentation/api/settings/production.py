from .app import AppSettings


class ProdAppSettings(AppSettings):
    db_user: str
    db_name: str
    db_password: str
    db_host: str
    db_port: str
    
    class Config(AppSettings.Config):
        env_file = "prod.env"
