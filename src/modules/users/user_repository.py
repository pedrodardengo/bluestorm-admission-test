from abc import ABC, abstractmethod
from typing import Optional

from src.modules.users.entities.user_entity import User


class UserRepository(ABC):
    @abstractmethod
    def add_user(self, username: str, salt_blank_hash: str) -> Optional[str]:
        ...

    @abstractmethod
    def find(self, username: str) -> Optional[User]:
        ...
