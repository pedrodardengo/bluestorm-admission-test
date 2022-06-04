from functools import lru_cache
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.config.database_conn import ENGINE
from src.patients.entities.patient import Patient
from src.patients.patient_repository import PatientRepository


class PatientRepositoryImpl(PatientRepository):
    def find_by_id(self, patient_id: str) -> Optional[Patient]:
        with Session(ENGINE) as session:
            statement = select(Patient).where(Patient.id == patient_id)
            return session.scalars(statement).one_or_none()


@lru_cache
def patient_repository_impl_factory() -> PatientRepositoryImpl:
    return PatientRepositoryImpl()
