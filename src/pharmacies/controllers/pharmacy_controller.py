from fastapi import APIRouter, Depends, Query

from src.auth.controllers.auth_controller import get_user_from_token
from src.exceptions.input import QueryParamsCantAllBeNone
from src.pharmacies.entities.pharmacy import Pharmacy
from src.pharmacies.services.phamarcy_service import (
    PharmacyService,
    pharmacy_service_factory,
)

pharmacy_router = APIRouter(
    prefix="/pharmacies", tags=["Pharmacy"], dependencies=[Depends(get_user_from_token)]
)


@pharmacy_router.get("/{pharmacy_id}")
async def get_pharmacy(
    pharmacy_id: str,
    pharmacy_service: PharmacyService = Depends(pharmacy_service_factory),
) -> Pharmacy:
    """
    Gets a single pharmacy by specifying the UUID of the pharmacy.
    """
    return pharmacy_service.get_pharmacy_by_id(pharmacy_id)


@pharmacy_router.get("/")
async def get_pharmacies(
    name: str = Query(None),
    city: str = Query(None),
    pharmacy_service: PharmacyService = Depends(pharmacy_service_factory),
) -> list[Pharmacy]:
    """
    Gets a list of pharmacies that may be queried by name of city.
    """
    if name is None and city is None:
        raise QueryParamsCantAllBeNone(["name", "city"])
    return pharmacy_service.get_pharmacies_where(name, city)
