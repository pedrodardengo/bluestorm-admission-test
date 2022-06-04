from fastapi import APIRouter, Depends, Query

from src.auth.controllers.auth_controller import get_user_from_token
from src.exceptions.input import QueryParamsCantAllBeNone
from src.transactions.entities.transaction import Transaction
from src.transactions.services.transaction_service import TransactionService, transaction_service_factory

transaction_router = APIRouter(
    prefix='/transactions',
    tags=['Transactions'],
    dependencies=[
        Depends(get_user_from_token)
    ]
)


@transaction_router.get('/')
async def get_transactions(
        patient_id: str = Query(None),
        pharmacy_id: str = Query(None),
        less_than: float = Query(None),
        more_than: float = Query(None),
        from_date: str = Query(None),
        to_date: str = Query(None),
        transaction_service: TransactionService = Depends(transaction_service_factory)
) -> list[Transaction]:
    if not any({patient_id, pharmacy_id, less_than, more_than, from_date, to_date}):
        raise QueryParamsCantAllBeNone(['patient_id', 'pharmacy_id', 'less_than', 'more_than', 'from_date', 'to_date'])
    return transaction_service.get_transactions_where(
        patient_id,
        pharmacy_id,
        less_than,
        more_than,
        from_date,
        to_date,
    )
