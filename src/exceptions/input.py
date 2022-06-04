

class QueryParamsCantAllBeNone(Exception):
    def __init__(self, params: str | list[str]):
        self.message = f"The query params {params} can't all be None."
        super().__init__()
