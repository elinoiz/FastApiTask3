from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
class Settings(BaseSettings):
    app_name: str = "new API"
    admin_email: str = "shwetsov27@gmail.com"
    POSTGRES_URLS: str = "postgresql://postgres:033150RRSQL@localhost:5432/movie"
    POSTGRES_URLA: str = "postgresql+asyncpg://postgres:033150RRSQL@localhost:5432/movie"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
load_dotenv()
settings = Settings()
settings.POSTGRES_PORT = int(os.environ.get('POSTGRES_PORT', 5432))
settings.POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '033150RRSQL')
settings.POSTGRES_DB = os.environ.get('POSTGRES_DB', 'movie')
settings.POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
settings.POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')

settings.POSTGRES_URLS = (
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)
settings.POSTGRES_URLA = (
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)