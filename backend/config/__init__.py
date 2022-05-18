from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "REST API CRUD"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_NAME: str = "users"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()