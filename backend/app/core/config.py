from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
SECRET_KEY: str = "fictitious_secret_key_change_me"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
STRIPE_SECRET_KEY: str = "sk_test_fictitious_XXXXXXXXXXXXXXXX"
STRIPE_WEBHOOK_SECRET: str = "whsec_fictitious_XXXXXXXXXXXXXXXX"

class Config:
        env_file = ".env"

settings = Settings()
