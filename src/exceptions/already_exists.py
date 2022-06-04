class AssetAlreadyExists(Exception):
    def __init__(self, asset: str, identifier_name: str, identifier: str):
        self.message = (
            f"The {asset} identified by {identifier_name}: {identifier} already exist."
        )
        super().__init__()


class UserAlreadyExists(AssetAlreadyExists):
    def __init__(self, identifier: str):
        super().__init__("user", "username", identifier)


class PharmacyAlreadyExists(AssetAlreadyExists):
    def __init__(self, identifier: str):
        super().__init__("pharmacy", "id", identifier)
