from pydantic import BaseSettings


class Settings(BaseSettings):
    es_cloud_id: str
    es_username: str
    es_password: str

    class Config:
        env_file = ".env"

settings = Settings()


