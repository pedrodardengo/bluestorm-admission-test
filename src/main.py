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

app = FastAPI(
    title="Admission Test for Bluestorm company",
    version="0.2.0",
    description=(
        "Essa é a implementação feita por **Pedro Dardengo Mesquita** do teste pedido pela empresa Bluestorm "
        "como parte de seu processo de seleção. Use **username: admin** e **password: Aa!!1111** na aba de Authorize "
        "para utilizar as funcionalidades protegidas."
    ),
    contact={
        "name": "Repositório Remoto do projeto",
        "url": "https://github.com/pedrodardengo/bluestorm-admission-test",
    },
)
app.add_exception_handler(Unauthorized, unauthorized_handler)
app.add_exception_handler(AssetAlreadyExists, already_exists_handler)
app.add_exception_handler(AssetNotFound, not_found_handler)
app.add_exception_handler(QueryParamsCantAllBeNone, empty_query_params_handler)

app.include_router(auth_controller.auth_router)
app.include_router(patient_controller.patient_router)
app.include_router(pharmacy_controller.pharmacy_router)
app.include_router(transaction_controller.transaction_router)
