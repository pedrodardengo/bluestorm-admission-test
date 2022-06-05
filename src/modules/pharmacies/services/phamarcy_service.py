from functools import lru_cache

from fastapi import Depends

from src.exceptions.not_found import PharmacyNotFound
from src.modules.pharmacies.entities.pharmacy import Pharmacy
from src.modules.pharmacies.pharmacy_repository import PharmacyRepository
from src.modules.pharmacies.repositories.pharmacy_repository_impl import (
    pharmacy_repository_impl_factory,
)


class PharmacyService:
    def __init__(self, pharmacy_repository: PharmacyRepository):
        self.__pharmacy_repo = pharmacy_repository

    def get_pharmacy_by_id(self, pharmacy_id: str) -> Pharmacy:
        pharmacy = self.__pharmacy_repo.find_by_id(pharmacy_id)
        if pharmacy is None:
            raise PharmacyNotFound(pharmacy_id)
        return pharmacy

    def get_pharmacies_where(
        self,
        name: str | None,
        city: str | None,
    ) -> list[Pharmacy]:
        return self.__pharmacy_repo.find_pharmacies_where(name, city)


@lru_cache
def pharmacy_service_factory(
    pharmacy_repository: PharmacyRepository = Depends(pharmacy_repository_impl_factory),
) -> PharmacyService:
    return PharmacyService(pharmacy_repository)
