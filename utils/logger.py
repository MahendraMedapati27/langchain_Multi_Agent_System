"""
Logging Configuration
"""
import sys
from loguru import logger
from config.settings import settings

def setup_logger():
    """Configure logger with appropriate settings."""
    # Remove default handler
    logger.remove()
    
    # Add console handler
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        level=settings.log_level,
        colorize=True
    )
    
    # Add file handler
    logger.add(
        str(settings.logs_dir / "app_{time:YYYY-MM-DD}.log"),
        rotation="00:00",
        retention="7 days",
        level=settings.log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}"
    )
    
    return logger

def get_logger(name: str):
    """Get a logger instance for a module."""
    setup_logger()
    return logger.bind(name=name)

