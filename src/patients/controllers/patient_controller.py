from fastapi import APIRouter, Depends

from src.auth.controllers.auth_controller import get_user_from_token
from src.patients.entities.patient import Patient
from src.patients.service.patient_service import patient_service_factory, PatientService

patient_router = APIRouter(
    prefix='/patient',
    tags=['Patients'],
    dependencies=[
        Depends(get_user_from_token)
    ]
)


@patient_router.get('/{patient_id}')
async def get_patient(
        patient_id: str,
        patient_service: PatientService = Depends(patient_service_factory)
) -> Patient:
    return patient_service.get_patient_by_id(patient_id)
