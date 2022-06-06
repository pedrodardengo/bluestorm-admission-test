import uvicorn
from fastapi import FastAPI

from src.exceptions.api_exception import APIException
from src.modules.auth.controllers import auth_controller
from src.exceptions.handlers import handle_api_exception
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
app.add_exception_handler(APIException, handle_api_exception)

app.include_router(auth_controller.auth_router)
app.include_router(patient_controller.patient_router)
app.include_router(pharmacy_controller.pharmacy_router)
app.include_router(transaction_controller.transaction_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        workers=1,
        reload=True,
    )
