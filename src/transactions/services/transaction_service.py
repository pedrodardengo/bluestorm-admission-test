from datetime import datetime
from functools import lru_cache

from fastapi import Depends

from src.transactions.entities.transaction import Transaction
from src.transactions.repositories.transaction_repository_impl import (
    transaction_repository_impl_factory,
)
from src.transactions.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository):
        self.__transaction_repo = transaction_repository

    def get_transactions_where(
        self,
        patient_id: str | None,
        pharmacy_id: str | None,
        less_than: float | None,
        more_than: float | None,
        after_date: str | None,
        before_date: str | None,
    ) -> list[Transaction]:
        after_datetime: datetime | None = None
        before_datetime: datetime | None = None
        if after_date is not None:
            after_datetime = datetime.strptime(after_date, "%Y-%m-%d %H:%M:%S")
        if before_date is not None:
            before_datetime = datetime.strptime(before_date, "%Y-%m-%d %H:%M:%S")
        return self.__transaction_repo.find_transactions_where(
            patient_id,
            pharmacy_id,
            less_than,
            more_than,
            after_datetime,
            before_datetime,
        )


@lru_cache
def transaction_service_factory(
    transaction_repository: TransactionRepository = Depends(
        transaction_repository_impl_factory
    ),
) -> TransactionService:
    return TransactionService(transaction_repository)
