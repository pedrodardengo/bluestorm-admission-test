

class AssetNotFound(Exception):
    def __init__(self, asset: str, identifier_name: str, identifier: str):
        self.message = f'The {asset} identified by {identifier_name}: {identifier} could not be found.'
        super().__init__()


class PharmacyNotFound(AssetNotFound):
    def __init__(self, identifier: str):
        super().__init__("pharmacy", "id", identifier)


class UserNotFound(AssetNotFound):
    def __init__(self, identifier: str):
        super().__init__("user", "username", identifier)


class PatientNotFound(AssetNotFound):
    def __init__(self, identifier: str):
        super().__init__("patient", "id", identifier)
