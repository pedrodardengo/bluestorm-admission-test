from datetime import datetime

from src.exceptions.input import CouldNotValidateDateString


def validate_and_parse_date(date_text: str | None) -> datetime | None:
    if date_text is None:
        return None
    try:
        return datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise CouldNotValidateDateString(date_text)
