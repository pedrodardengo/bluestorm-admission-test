from sqlalchemy import Column, String
from src.config.database_conn import Base
from src.tools.password_tools import verify_password


class User(Base):
    __tablename__ = 'USERS'

    id: str = Column('UUID', String, primary_key=True)
    username = Column('USERNAME', String)
    salted_hash: str = Column('PASSWORD', String)

    def is_password_valid(self, salted_hash: str) -> bool:
        salt, hashed_password = self.salted_hash.split(" ")
        return verify_password(salted_hash, salt, hashed_password)
