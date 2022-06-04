from datetime import datetime
from functools import lru_cache

from fastapi import Depends

from src.transactions.entities.transaction import Transaction
from src.transactions.repositories.transaction_repository_impl import transaction_repository_impl_factory
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
            from_date: str | None,
            to_date: str | None,
    ) -> list[Transaction]:
        if from_date is not None:
            from_date = datetime.strptime(from_date, '%Y-%m-%d %H:%M:%S')
        if to_date is not None:
            to_date = datetime.strptime(to_date, '%Y-%m-%d %H:%M:%S')
        return self.__transaction_repo.find_transactions_where(
            patient_id,
            pharmacy_id,
            less_than,
            more_than,
            from_date,
            to_date,
        )


@lru_cache
def transaction_service_factory(
        transaction_repository: TransactionRepository = Depends(transaction_repository_impl_factory)
) -> TransactionService:
    return TransactionService(transaction_repository)