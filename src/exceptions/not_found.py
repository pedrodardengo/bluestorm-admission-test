class AssetNotFound(Exception):
    def __init__(self) -> None:
        self.message: str
        super().__init__()

    @staticmethod
    def generate_base_message(asset: str, identifier_name: str, identifier: str) -> str:
        return f"The {asset} identified by {identifier_name}: {identifier} could not be found."


class PharmacyNotFound(AssetNotFound):
    def __init__(self, identifier: str) -> None:
        super().__init__()
        self.message = self.generate_message(identifier)

    @staticmethod
    def generate_message(identifier: str) -> str:
        return AssetNotFound.generate_base_message("pharmacy", "id", identifier)


class UserNotFound(AssetNotFound):
    def __init__(self, identifier: str) -> None:
        super().__init__()
        self.message = self.generate_message(identifier)

    @staticmethod
    def generate_message(identifier: str) -> str:
        return AssetNotFound.generate_base_message("user", "username", identifier)


class PatientNotFound(AssetNotFound):
    def __init__(self, identifier: str) -> None:
        super().__init__()
        self.message = self.generate_message(identifier)

    @staticmethod
    def generate_message(identifier: str) -> str:
        return AssetNotFound.generate_base_message("patient", "id", identifier)


class TransactionNotFound(AssetNotFound):
    def __init__(self, identifier: str) -> None:
        super().__init__()
        self.message = self.generate_message(identifier)

    @staticmethod
    def generate_message(identifier: str) -> str:
        return AssetNotFound.generate_base_message("transaction", "id", identifier)
