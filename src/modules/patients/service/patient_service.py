from functools import lru_cache

from fastapi import Depends

from src.exceptions.not_found import PatientNotFound
from src.modules.patients.entities.patient import Patient
from src.modules.patients.patient_repository import PatientRepository
from src.modules.patients.repositories.patient_repository_impl import (
    patient_repository_impl_factory,
)


class PatientService:
    def __init__(self, patient_repository: PatientRepository):
        self.__patient_repo = patient_repository

    def get_patient_by_id(self, patient_id: str) -> Patient:
        patient = self.__patient_repo.find_by_id(patient_id)
        if patient is None:
            raise PatientNotFound(patient_id)
        return patient


@lru_cache()
def patient_service_factory(
    patient_repository: PatientRepository = Depends(patient_repository_impl_factory),
) -> PatientService:
    return PatientService(patient_repository)
