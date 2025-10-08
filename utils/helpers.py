from datetime import datetime, timedelta
from typing import Optional, Any
import hashlib
import secrets
from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hashed password
    """
    return pwd_context.verify(plain_password, hashed_password)


def generate_token(length: int = 32) -> str:
    """
    Generate a random token
    """
    return secrets.token_urlsafe(length)


def hash_string(value: str) -> str:
    """
    Generate SHA256 hash of a string
    """
    return hashlib.sha256(value.encode()).hexdigest()


def calculate_pagination(page: int, page_size: int, total_items: int) -> dict:
    """
    Calculate pagination metadata
    """
    total_pages = (total_items + page_size - 1) // page_size
    
    return {
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1
    }


def get_offset_limit(page: int, page_size: int) -> tuple:
    """
    Calculate offset and limit for database queries
    """
    offset = (page - 1) * page_size
    return offset, page_size


def datetime_to_timestamp(dt: datetime) -> int:
    """
    Convert datetime to Unix timestamp
    """
    return int(dt.timestamp())


def timestamp_to_datetime(timestamp: int) -> datetime:
    """
    Convert Unix timestamp to datetime
    """
    return datetime.fromtimestamp(timestamp)


def format_datetime(dt: Optional[datetime], format_str: str = "%Y-%m-%d %H:%M:%S") -> Optional[str]:
    """
    Format datetime to string
    """
    if dt:
        return dt.strftime(format_str)
    return None


def is_expired(expiry_time: datetime) -> bool:
    """
    Check if a datetime has expired
    """
    return datetime.utcnow() > expiry_time


def add_time(dt: Optional[datetime] = None, **kwargs) -> datetime:
    """
    Add time to a datetime (default: now)
    Usage: add_time(hours=1, minutes=30)
    """
    if dt is None:
        dt = datetime.utcnow()
    return dt + timedelta(**kwargs)

