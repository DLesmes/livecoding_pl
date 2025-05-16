from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from dotenv import load_dotenv

# Load .env from project root if this script is in app/
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else: # try loading from current dir (if script run from root)
    load_dotenv()


class Settings(BaseSettings):
    app_name: str = "FastAPI LangChain App"
    debug: bool = False
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "") # Important: Load from env
    
    class Config:
        env_file = ".env" # This is relative to where settings.py is or where app runs from
        extra = "ignore"


@lru_cache()
def get_settings():
    s = Settings()
    if not s.google_api_key:
        print("Warning: GOOGLE_API_KEY not loaded. Check .env file and its path.")
    return s