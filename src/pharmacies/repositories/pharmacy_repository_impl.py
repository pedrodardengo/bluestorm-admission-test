from functools import lru_cache
from typing import Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from src.config.database_conn import db_engine_factory
from src.pharmacies.entities.pharmacy import Pharmacy
from src.pharmacies.pharmacy_repository import PharmacyRepository


class PharmacyRepositoryImpl(PharmacyRepository):
    def __init__(self, engine: Engine):
        self.__engine = engine

    def find_pharmacies_where(
        self,
        name: str | None,
        city: str | None,
    ) -> list[Pharmacy]:
        with Session(self.__engine) as session:
            statement = select(Pharmacy)
            if name is not None:
                statement = statement.where(Pharmacy.name == name)
            if city is not None:
                statement = statement.where(Pharmacy.city == city)
            return list(session.scalars(statement))

    def find_by_id(self, pharmacy_id: str) -> Optional[Pharmacy]:
        with Session(self.__engine) as session:
            statement = select(Pharmacy).where(Pharmacy.id == pharmacy_id)
            return session.scalars(statement).one_or_none()


@lru_cache
def pharmacy_repository_impl_factory(
    db_engine: Engine = Depends(db_engine_factory),
) -> PharmacyRepositoryImpl:
    return PharmacyRepositoryImpl(db_engine)
