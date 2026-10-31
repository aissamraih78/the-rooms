"""
SyntaxCraft Studio - Pipeline Configuration Module
Manages environment variables, rate limits, and service credentials.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "SyntaxCraft SEO & Automation Pipeline"
    environment: str = "production"
    log_level: str = "INFO"
    
    # Concurrency and Rate Limits
    max_concurrent_workers: int = Field(default=5, ge=1, le=20)
    request_timeout_sec: float = 12.0
    retry_attempts: int = 3
    retry_backoff_factor: float = 1.5
    
    # Public Metrics Endpoints
    target_catalog_endpoint: str = "https://api.public-market.io/v2/catalog"
    database_sqlite_path: str = "data/analytics.db"
    
    # Webhook & Integration Configuration
    webhook_host: str = "0.0.0.0"
    webhook_port: int = 8080
    webhook_secret: str = "change_me_in_production_secret_token"
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

