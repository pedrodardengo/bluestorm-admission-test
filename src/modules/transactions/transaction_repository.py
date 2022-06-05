from abc import ABC, abstractmethod
from datetime import datetime

from src.modules.transactions.entities.transaction import Transaction


class TransactionRepository(ABC):
    @abstractmethod
    def find_transactions_where(
        self,
        patient_id: str | None,
        pharmacy_id: str | None,
        less_than: float | None,
        more_than: float | None,
        after_date: datetime | None,
        before_date: datetime | None,
    ) -> list[Transaction]:
        ...

    @abstractmethod
    def find_transactions_by_id(self, transaction_id: str) -> Transaction:
        ...
