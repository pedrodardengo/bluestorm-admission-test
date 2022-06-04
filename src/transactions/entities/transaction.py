from sqlalchemy import String, Float, Date, ForeignKey, Column
from sqlalchemy.orm import relationship

from src.config.database_conn import Base


class Transaction(Base):
    __tablename__ = 'TRANSACTIONS'

    id: str = Column('UUID', String, primary_key=True)
    patient_id: str = Column('PATIENT_UUID', ForeignKey('USERS.UUID'))
    pharmacy_id: str = Column('PHARMACY_UUID', ForeignKey('PHARMACY.UUID'))
    amount: float = Column('AMOUNT', Float)
    timestamp: str = Column('TIMESTAMP', Date)

    patient = relationship("Patient", back_populates="transactions")
    pharmacy = relationship('Pharmacy', back_populates='transactions')
