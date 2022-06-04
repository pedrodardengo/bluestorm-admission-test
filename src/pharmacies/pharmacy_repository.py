from abc import ABC, abstractmethod
from typing import Optional

from src.pharmacies.entities.pharmacy import Pharmacy


class PharmacyRepository(ABC):
    @abstractmethod
    def find_pharmacies_where(
        self,
        name: str | None,
        city: str | None,
    ) -> list[Pharmacy]:
        ...

    @abstractmethod
    def find_by_id(self, pharmacy_id: str) -> Optional[Pharmacy]:
        ...
