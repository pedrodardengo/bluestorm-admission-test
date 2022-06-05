from pydantic import BaseModel, validator
from pydantic.class_validators import Optional

from src.tools.password_tools import check_password_strength, get_hash, get_salt


class IncomingUserDTO(BaseModel):
    username: str
    password: str

    @validator("password")
    def password_must_be_strong(cls, password):
        return check_password_strength(password)

    def get_salted_hash(self, salt: Optional[str] = None):
        if salt is None:
            salt = get_salt()
        hashed_password = get_hash(self.password + salt)
        return f"{salt} {hashed_password}"

    class Config:
        schema_extra = (
            {
                "normal": {
                    "summary": "An accepted user password",
                    "description": "The password is strong enough for the sign-up process",
                    "value": {"username": "pedro", "password": "Aa!!1111"},
                },
                "invalid": {
                    "summary": "Invalid Password",
                    "description": "The password is not strong enough for the sign-up process",
                    "value": {"username": "pedro", "password": "Aa!!1111"},
                },
            },
        )
