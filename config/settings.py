"""
Application Configuration
"""
import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # API Keys
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    
    # LangSmith (optional)
    langchain_tracing_v2: bool = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
    langchain_api_key: Optional[str] = os.getenv("LANGCHAIN_API_KEY")
    langchain_project: str = os.getenv("LANGCHAIN_PROJECT", "langgraph-multi-agent")
    
    # Application Settings
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    max_retries: int = int(os.getenv("MAX_RETRIES", "3"))
    timeout_seconds: int = int(os.getenv("TIMEOUT_SECONDS", "30"))
    
    # Model Configurations
    default_model: str = "llama-3.3-70b-versatile"  # Groq model
    cheap_model: str = "llama-3.1-8b-instant"  # Groq fast model
    fast_model: str = "gemini-2.0-flash-exp"  # Google model
    
    # Paths
    base_dir: Path = Path(__file__).parent.parent
    logs_dir: Path = base_dir / "logs"
    
    class Config:
        env_file = ".env"
        case_sensitive = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create logs directory if it doesn't exist
        self.logs_dir.mkdir(exist_ok=True)
    
    def validate_api_keys(self) -> bool:
        """Check if required API keys are set."""
        if not self.groq_api_key:
            return False
        return True

# Create logs directory before instantiating settings
logs_dir = Path(__file__).parent.parent / "logs"
logs_dir.mkdir(exist_ok=True)

# Global settings instance
settings = Settings()

