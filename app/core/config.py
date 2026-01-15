from pydantic_settings import BaseSettings

class Config(BaseSettings):
    APP_NAME: str = "FastAPI App"
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    ENV: str = "development"  # development | production

    class Config:
        env_file = ".env"

config = Config()