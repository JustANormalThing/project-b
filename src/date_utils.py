from datetime import date, timedelta


def get_current_date() -> date:
    """Возвращает текущую дату."""
    return date.today()


def format_date(value: date, format_string: str = "%d.%m.%Y") -> str:
    """Форматирует дату в строку."""
    return value.strftime(format_string)


def days_between(first: date, second: date) -> int:
    """Возвращает количество дней между двумя датами."""
    return abs((second - first).days)


def add_days(value: date, days: int) -> date:
    """Добавляет указанное количество дней к дате."""
    return value + timedelta(days=days)
