from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "wiki_telegram_bot"
    POSTGRESQL_HOSTNAME: str = "localhost"
    POSTGRESQL_USERNAME: str = "postgres"
    POSTGRESQL_PASSWORD: str = ""
    POSTGRESQL_DATABASE: str = "wiki"


settings = Settings()

TOKEN = "5352606139:AAEvCu4Vp7j4eYnssbTeHtbCcLwyxBvpp5M"
