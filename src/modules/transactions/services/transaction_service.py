from datetime import datetime
from functools import lru_cache

from fastapi import Depends

from src.exceptions.not_found import TransactionNotFound
from src.modules.transactions.entities.transaction import Transaction
from src.modules.transactions.repositories.transaction_repository_impl import (
    transaction_repository_impl_factory,
)
from src.modules.transactions.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository):
        self.__transaction_repo = transaction_repository

    def get_transaction_by_id(self, transaction_id: str) -> Transaction:
        transaction = self.__transaction_repo.find_transactions_by_id(transaction_id)
        if transaction is None:
            raise TransactionNotFound(transaction_id)
        return transaction

    def get_transactions_where(
        self,
        patient_id: str | None,
        pharmacy_id: str | None,
        less_than: float | None,
        more_than: float | None,
        after_date: datetime | None,
        before_date: datetime | None,
    ) -> list[Transaction]:
        return self.__transaction_repo.find_transactions_where(
            patient_id,
            pharmacy_id,
            less_than,
            more_than,
            after_date,
            before_date,
        )


@lru_cache
def transaction_service_factory(
    transaction_repository: TransactionRepository = Depends(
        transaction_repository_impl_factory
    ),
) -> TransactionService:
    return TransactionService(transaction_repository)
