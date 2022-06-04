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
        after_date: str = Query(None),
        before_date: str = Query(None),
        transaction_service: TransactionService = Depends(transaction_service_factory)
) -> list[Transaction]:
    """
    Gets a list of transactions that may be queried by the UUID of the pharmacy or of the patient, by transactions that
    have amounts greater of smaller than a certain value, before a certain date or after a certain date
    (date should ONLY be expressed in this format 2019-02-25 20:30:54).
    """
    if not any({patient_id, pharmacy_id, less_than, more_than, after_date, before_date}):
        raise QueryParamsCantAllBeNone(
            ['patient_id', 'pharmacy_id', 'less_than', 'more_than', 'after_date', 'before_date']
        )
    return transaction_service.get_transactions_where(
        patient_id,
        pharmacy_id,
        less_than,
        more_than,
        after_date,
        before_date,
    )
