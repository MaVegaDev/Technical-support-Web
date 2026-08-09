from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class technician(Base):
    __tablename__ = 'technician'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    user = relationship('User', back_populates='technician')
    service_orders = relationship('ServiceOrder',  back_populates='technician')
    