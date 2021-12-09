import secrets

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # StarkWare
    SEQUENCER: AnyHttpUrl

    PROJECT_NAME: str

    class Config:
        case_sensitive = True


settings = Settings()
