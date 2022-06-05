from functools import lru_cache
from typing import Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from src.config.database_conn import db_engine_factory
from src.patients.entities.patient import Patient
from src.patients.patient_repository import PatientRepository


class PatientRepositoryImpl(PatientRepository):
    def __init__(self, engine: Engine):
        self.__engine = engine

    def find_by_id(self, patient_id: str) -> Optional[Patient]:
        with Session(self.__engine) as session:
            statement = select(Patient).where(Patient.id == patient_id)
            return session.scalars(statement).one_or_none()


@lru_cache
def patient_repository_impl_factory(
    db_engine: Engine = Depends(db_engine_factory),
) -> PatientRepositoryImpl:
    return PatientRepositoryImpl(db_engine)
