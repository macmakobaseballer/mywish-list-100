from pydantic import BaseSettings

# looks at them as a case-insensitive (validate them)
# default values provided
class Settings(BaseSettings):
    DYN_ENDPOINT_URL: str
    DYN_REGION_NAME: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()

