from functools import lru_cache

from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime
from src.config.database_conn import ENGINE
from src.transactions.entities.transaction import Transaction
from src.transactions.transaction_repository import TransactionRepository


class TransactionRepositoryImpl(TransactionRepository):

    def find_transactions_where(
            self,
            patient_id: str | None,
            pharmacy_id: str | None,
            less_than: float | None,
            more_than: float | None,
            from_date: datetime | None,
            to_date: datetime | None,
    ) -> list[Transaction]:
        with Session(ENGINE) as session:
            statement = select(Transaction)
            if patient_id is not None:
                statement = statement.where(Transaction.patient_id == patient_id)
            if pharmacy_id is not None:
                statement = statement.where(Transaction.pharmacy_id == pharmacy_id)
            if less_than is not None:
                statement = statement.where(Transaction.amount <= less_than)
            if more_than is not None:
                statement = statement.where(Transaction.amount >= more_than)
            if from_date is not None:
                statement = statement.where(Transaction.timestamp >= from_date)
            if to_date is not None:
                statement = statement.where(Transaction.timestamp <= to_date)
            statement = statement.join(Transaction.patient).join(Transaction.pharmacy)
            return list(session.scalars(statement))


@lru_cache
def transaction_repository_impl_factory() -> TransactionRepositoryImpl:
    return TransactionRepositoryImpl()
