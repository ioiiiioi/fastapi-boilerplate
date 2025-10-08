from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Any, Dict
from datetime import datetime


class BaseSerializer(BaseModel):
    """
    Base serializer with common configuration
    """
    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        arbitrary_types_allowed=True
    )


class ResponseSerializer(BaseSerializer):
    """
    Standard API response serializer
    """
    success: bool = True
    message: Optional[str] = None
    data: Optional[Any] = None
    errors: Optional[Dict[str, Any]] = None


class PaginationSerializer(BaseSerializer):
    """
    Pagination metadata serializer
    """
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=10, ge=1, le=100)
    total_items: int = 0
    total_pages: int = 0


class PaginatedResponseSerializer(BaseSerializer):
    """
    Paginated response serializer
    """
    success: bool = True
    data: list = []
    pagination: PaginationSerializer


class TimestampMixin(BaseModel):
    """
    Mixin for timestamp fields
    """
    created_at: datetime
    updated_at: datetime


class IDMixin(BaseModel):
    """
    Mixin for ID field
    """
    id: int = Field(..., description="Unique identifier")


# Example serializers for common use cases

class HealthCheckSerializer(BaseSerializer):
    """
    Health check response serializer
    """
    status: str
    database: Optional[str] = None
    cache: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ErrorSerializer(BaseSerializer):
    """
    Error response serializer
    """
    success: bool = False
    message: str
    error_code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

