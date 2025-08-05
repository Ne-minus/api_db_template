from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Database settings

    postgres_host: str = Field("localhost", title="Хост")
    postgres_port: int = Field(5432, title="Порт")
    postgres_user: str = Field("postgres", title="Пользователь")
    postgres_password: str = Field(..., title="Пароль")
    postgres_db: str = Field("db", title="База данных")

    # model_config = SettingsConfigDict(
    #     env_file=".env"
    # )


settings = Settings()
