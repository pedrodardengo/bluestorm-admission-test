from fastapi import APIRouter, Depends

from src.modules.auth.controllers.auth_controller import get_user_from_token
from src.modules.patients.entities.patient import Patient
from src.modules.patients.service.patient_service import (
    PatientService,
    patient_service_factory,
)


PATIENTS_URL = "/patients"
patient_router = APIRouter(
    prefix=PATIENTS_URL, tags=["Patients"], dependencies=[Depends(get_user_from_token)]
)


@patient_router.get("/{patient_id}")
async def get_patient(
    patient_id: str, patient_service: PatientService = Depends(patient_service_factory)
) -> Patient:
    """
    Gets a single patient by specifying the UUID of the patient.
    """
    return patient_service.get_patient_by_id(patient_id)
