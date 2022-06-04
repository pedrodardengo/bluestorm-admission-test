from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from src.config.database_conn import Base


class Pharmacy(Base):
    __tablename__ = "PHARMACIES"
    id: str = Column("UUID", String, primary_key=True)
    name = Column("NAME", String)
    city = Column("CITY", String)

    transactions = relationship(
        "Transaction", back_populates="pharmacy", cascade="all, delete-orphan"
    )
