from datetime import date, datetime

from model.fields.base_field import Field

BIRTHDAY_PATTERN = "%d.%m.%Y"


class Birthday(Field):
    def __init__(self, value: str):
        self.__date = self.__parse(value)
        super().__init__("birthday", self.__date.strftime(BIRTHDAY_PATTERN))

    def get_next_birthday(self) -> date:
        today = date.today()
        try:
            next_birthday = self.__date.replace(year=today.year)
        except ValueError:
            next_birthday = date(today.year, 2, 28)
        if next_birthday < today:
            try:
                return next_birthday.replace(year=today.year + 1)
            except ValueError:
                return date(today.year + 1, 2, 28)
        return next_birthday

    @staticmethod
    def __parse(value: str) -> date:
        try:
            return datetime.strptime(value, BIRTHDAY_PATTERN).date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
