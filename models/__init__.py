from service.database import Base
from models.base import BaseModel
from models.user import User

# Import all models here for Alembic to detect them
__all__ = ["Base", "BaseModel", "User"]

