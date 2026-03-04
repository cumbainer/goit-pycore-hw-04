from model.fields.base_field import Field

PHONE_NUMBER_LENGTH = 10


class Phone(Field):
    def __init__(self, value: str):
        if not self.__is_valid(value):
            raise ValueError("Phone number must be 10 digits.")
        super().__init__("phone", value)
        self.__number = value

    @property
    def number(self) -> str:
        return self.__number

    @staticmethod
    def __is_valid(phone_number: str) -> bool:
        return isinstance(phone_number, str) and len(phone_number) == PHONE_NUMBER_LENGTH and phone_number.isdigit()

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.__number == other.number
        return False

    def __str__(self):
        return self.__number

    def __repr__(self):
        return str(self)
