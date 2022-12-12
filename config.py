from pydantic import BaseSettings


class Config(BaseSettings):
    TOKEN: str
    WEBHOOK_URL_PATH: str = None
    WEBHOOK_SSL_CERT: str = None
    WEBHOOK_SSL_PRIV: str = None

    SECRET: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    ADMIN_USERNAME: str
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    class Config:
        case_sensitive = True
