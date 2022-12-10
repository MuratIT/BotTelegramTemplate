from pydantic import BaseSettings


class Config(BaseSettings):
    TOKEN: str = ""
    DATABASE_URL: str = ""

    class Config:
        case_sensitive = True
