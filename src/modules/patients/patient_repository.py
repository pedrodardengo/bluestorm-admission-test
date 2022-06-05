from abc import ABC, abstractmethod
from typing import Optional

from src.modules.patients.entities.patient import Patient


class PatientRepository(ABC):
    @abstractmethod
    def find_by_id(self, patient_id: str) -> Optional[Patient]:
        ...
