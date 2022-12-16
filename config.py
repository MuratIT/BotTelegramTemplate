from pydantic import BaseSettings


class Config(BaseSettings):
    TOKEN: str

    SKIP_UPDATES: bool = True

    WEBHOOK_URL: str
    WEBHOOK_SSL_CERT: str = None

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    class Config:
        case_sensitive = True
