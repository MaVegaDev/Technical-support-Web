from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, unique=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default='client') #Only the roles 'Admin', 'technician' and client
    is_active = Column(Boolean, default=True)

    technician = relationship('Technician', back_populates='user', uselist=False)
    service_orders = relationship('ServiceOrder', back_populates='client', foreign_keys="ServiceOrder.client_id")
