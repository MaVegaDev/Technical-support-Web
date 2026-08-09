from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class ServiceOrder(Base):
    __tablename__ = 'service_orders'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    status = Column(String, default='pending') #Only the status pending, in_progress, paused, complete, cancelled
    priority = Column(String, default='low') #Only the priorities low, mid, high and urgent
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    client_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    technician_id = Column(Integer, ForeignKey('technician.id'), nullable=True)

    client = relationship('User', back_populates='service_orders', foreign_keys=[client_id])
    technician = relationship('Technician', back_populates='service_orders')

    