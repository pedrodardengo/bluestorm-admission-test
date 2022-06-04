
from abc import ABC, abstractmethod
from datetime import datetime

from src.transactions.entities.transaction import Transaction


class TransactionRepository(ABC):

    @abstractmethod
    def find_transactions_where(
            self,
            patient_id: str | None,
            pharmacy_id: str | None,
            less_than: float | None,
            more_than: float | None,
            from_date: datetime | None,
            to_date: datetime | None,
    ) -> list[Transaction]:
        ...