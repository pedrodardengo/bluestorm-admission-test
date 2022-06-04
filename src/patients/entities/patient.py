from sqlalchemy import String, Date, Column
from sqlalchemy.orm import relationship

from src.config.database_conn import Base


class Patient(Base):
    __tablename__ = 'PATIENTS'

    id: str = Column('UUID', String, primary_key=True)
    first_name: str = Column('FIRST_NAME', String)
    last_name: str = Column('LAST_NAME', String)
    birth_date: str = Column('DATE_OF_BIRTH', Date)

    transactions = relationship("Transaction", back_populates="patient", cascade="all, delete-orphan")
