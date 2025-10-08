from sqlalchemy import Column, Integer, DateTime, func
from service.database import Base


class BaseModel(Base):
    """
    Base model class with common fields
    """
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    def to_dict(self):
        """
        Convert model instance to dictionary
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

