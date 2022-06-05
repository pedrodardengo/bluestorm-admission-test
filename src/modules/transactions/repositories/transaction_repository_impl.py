from datetime import datetime
from functools import lru_cache

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from src.config.database_conn import db_engine_factory
from src.modules.transactions.entities.transaction import Transaction
from src.modules.transactions.transaction_repository import TransactionRepository


class TransactionRepositoryImpl(TransactionRepository):
    def __init__(self, engine: Engine):
        self.__engine = engine

    def find_transactions_by_id(self, transaction_id: str) -> Transaction:
        with Session(self.__engine) as session:
            statement = select(Transaction).where(Transaction.id == transaction_id)
            return session.scalars(statement).one_or_none()

    def find_transactions_where(
        self,
        patient_id: str | None,
        pharmacy_id: str | None,
        less_than: float | None,
        more_than: float | None,
        after_date: datetime | None,
        before_date: datetime | None,
    ) -> list[Transaction]:
        with Session(self.__engine) as session:
            statement = select(Transaction)
            if patient_id is not None:
                statement = statement.where(Transaction.patient_id == patient_id)
            if pharmacy_id is not None:
                statement = statement.where(Transaction.pharmacy_id == pharmacy_id)
            if less_than is not None:
                statement = statement.where(Transaction.amount <= less_than)
            if more_than is not None:
                statement = statement.where(Transaction.amount >= more_than)
            if after_date is not None:
                statement = statement.where(Transaction.timestamp >= after_date)
            if before_date is not None:
                statement = statement.where(Transaction.timestamp <= before_date)
            statement = statement.join(Transaction.patient).join(Transaction.pharmacy)
            return list(session.scalars(statement))


@lru_cache
def transaction_repository_impl_factory(
    db_engine: Engine = Depends(db_engine_factory),
) -> TransactionRepositoryImpl:
    return TransactionRepositoryImpl(db_engine)
