import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FlavorFusion AI"
    API_V1_STR: str = "/api"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-flavor-fusion-secret-key-change-in-production-2026")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Database setup: SQLite fallback or production PostgreSQL
    _backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    _default_db = os.path.join(_backend_dir, "flavorfusion.db").replace("\\", "/")
    
    _raw_db = os.getenv("DATABASE_URL")
    if _raw_db:
        # Normalize postgres:// to postgresql:// for SQLAlchemy compatibility
        if _raw_db.startswith("postgres://"):
            _raw_db = _raw_db.replace("postgres://", "postgresql://", 1)
        DATABASE_URL: str = _raw_db
    elif os.getenv("VERCEL"):
        # On Vercel serverless, filesystem is read-only outside /tmp
        import shutil
        _tmp_db = "/tmp/flavorfusion.db"
        if not os.path.exists(_tmp_db) and os.path.exists(_default_db):
            try:
                shutil.copyfile(_default_db, _tmp_db)
            except Exception as e:
                print(f"Notice: /tmp copy exception: {e}")
        DATABASE_URL: str = f"sqlite:///{_tmp_db}"
    else:
        DATABASE_URL: str = f"sqlite:///{_default_db}"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "*"
    ]
    
    # Optional LLM integration (Gemini)
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # Uploads (use /tmp on Vercel)
    if os.getenv("VERCEL"):
        UPLOAD_DIR: str = "/tmp/uploads"
    else:
        UPLOAD_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "uploads")
    MAX_UPLOAD_SIZE_MB: int = 10
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
