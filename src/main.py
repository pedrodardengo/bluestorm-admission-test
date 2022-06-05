import os

import uvicorn
from fastapi import FastAPI

from src.modules.auth.controllers import auth_controller
from src.exceptions.already_exists import AssetAlreadyExists
from src.exceptions.auth import Unauthorized
from src.exceptions.handlers import (
    already_exists_handler,
    empty_query_params_handler,
    not_found_handler,
    unauthorized_handler,
)
from src.exceptions.input import QueryParamsCantAllBeNone
from src.exceptions.not_found import AssetNotFound
from src.modules.patients.controllers import patient_controller
from src.modules.pharmacies.controllers import pharmacy_controller
from src.modules.transactions.controllers import transaction_controller

app = FastAPI(title="Admission test for Bluestorm company", version="0.1.0")

app.add_exception_handler(Unauthorized, unauthorized_handler)
app.add_exception_handler(AssetAlreadyExists, already_exists_handler)
app.add_exception_handler(AssetNotFound, not_found_handler)
app.add_exception_handler(QueryParamsCantAllBeNone, empty_query_params_handler)

app.include_router(auth_controller.auth_router)
app.include_router(patient_controller.patient_router)
app.include_router(pharmacy_controller.pharmacy_router)
app.include_router(transaction_controller.transaction_router)

if __name__ == "__main__":
    os.environ["TOKEN_SECRET"] = "AFakeTokenSecret"
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        workers=1,
        reload=True,
    )
