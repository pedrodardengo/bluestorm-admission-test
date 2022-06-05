from fastapi import APIRouter, Depends, Query

from src.modules.auth.controllers.auth_controller import get_user_from_token
from src.exceptions.input import QueryParamsCantAllBeNone
from src.modules.pharmacies.entities.pharmacy import Pharmacy
from src.modules.pharmacies.services.phamarcy_service import (
    PharmacyService,
    pharmacy_service_factory,
)

PHARMACIES_URL = "/pharmacies"
pharmacy_router = APIRouter(
    prefix=PHARMACIES_URL,
    tags=["Pharmacy"],
    dependencies=[Depends(get_user_from_token)],
)


@pharmacy_router.get("/")
async def get_pharmacies(
    pharmacy_id: str = Query(None),
    name: str = Query(None),
    city: str = Query(None),
    pharmacy_service: PharmacyService = Depends(pharmacy_service_factory),
) -> Pharmacy | list[Pharmacy]:
    """
    Gets a list of pharmacies that may be queried by name of city.
    """
    if not any({pharmacy_id, name, city}):
        raise QueryParamsCantAllBeNone(["pharmacy_id", "name", "city"])
    if pharmacy_id is not None:
        return pharmacy_service.get_pharmacy_by_id(pharmacy_id)
    return pharmacy_service.get_pharmacies_where(name, city)
