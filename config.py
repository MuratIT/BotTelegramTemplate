from pydantic import BaseSettings


class Config(BaseSettings):
    token: str = ""
    dataBaseURL: str = ""

    class Config:
        case_sensitive = True
