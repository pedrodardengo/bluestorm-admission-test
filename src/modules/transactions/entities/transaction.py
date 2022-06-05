from sqlalchemy import Column, Date, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from src.config.database_conn import Base


class Transaction(Base):
    __tablename__ = "TRANSACTIONS"

    id: str = Column("UUID", String, primary_key=True)
    patient_id: str = Column("PATIENT_UUID", ForeignKey("PATIENTS.UUID"))
    pharmacy_id: str = Column("PHARMACY_UUID", ForeignKey("PHARMACIES.UUID"))
    amount: float = Column("AMOUNT", Float)
    timestamp: Date = Column("TIMESTAMP", Date)

    patient = relationship("Patient", back_populates="transactions", lazy="joined")
    pharmacy = relationship("Pharmacy", back_populates="transactions", lazy="joined")
