from fastapi import APIRouter, Depends, Query

from src.modules.auth.controllers.auth_controller import get_user_from_token
from src.exceptions.input import QueryParamsCantAllBeNone
from src.modules.transactions.entities.transaction import Transaction
from src.modules.transactions.services.transaction_service import (
    TransactionService,
    transaction_service_factory,
)
from src.tools.date_tools import validate_and_parse_date

TRANSACTIONS_URL = "/transactions"

transaction_router = APIRouter(
    prefix=TRANSACTIONS_URL,
    tags=["Transactions"],
    dependencies=[Depends(get_user_from_token)],
)


@transaction_router.get("/")
async def get_transactions(
    transaction_id: str = Query(None),
    patient_id: str = Query(None),
    pharmacy_id: str = Query(None),
    less_than: float = Query(None),
    more_than: float = Query(None),
    after_date: str = Query(None),
    before_date: str = Query(None),
    transaction_service: TransactionService = Depends(transaction_service_factory),
) -> Transaction | list[Transaction]:
    """
    Gets a list of transactions that may be queried by the UUID of the pharmacy or of the patient, by transactions that
    have amounts greater of smaller than a certain value, before a certain date or after a certain date
    (date should ONLY be expressed in this format 2019-02-25 20:30:54).
    """
    if not any(
        {
            transaction_id,
            patient_id,
            pharmacy_id,
            less_than,
            more_than,
            after_date,
            before_date,
        }
    ):
        raise QueryParamsCantAllBeNone(
            [
                "transaction_id" "patient_id",
                "pharmacy_id",
                "less_than",
                "more_than",
                "after_date",
                "before_date",
            ]
        )
    if transaction_id is not None:
        return transaction_service.get_transaction_by_id(transaction_id)

    return transaction_service.get_transactions_where(
        patient_id,
        pharmacy_id,
        less_than,
        more_than,
        validate_and_parse_date(after_date),
        validate_and_parse_date(before_date),
    )
