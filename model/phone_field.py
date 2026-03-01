from argparse import ArgumentError

from model.base_field import Field

PHONE_FIELD_ID = "phone"
PHONE_NUMBER_LENGTH = 10


class PhoneField(Field):
    def __init__(self, value: int):
        super().__init__(PHONE_FIELD_ID, str(value))
        self.__number = value
        is_phone_number_valid = self.__is_phone_number_valid(value)
        if not is_phone_number_valid:
            raise RuntimeError("Invalid phone number.")

    @property
    def number(self) -> int:
        return self.__number

    @staticmethod
    def __is_phone_number_valid(phone_number: int) -> bool:
        if not phone_number:
            return False

        try:
            str_phone_number = str(phone_number)
            number_length = len(str_phone_number)
            if number_length != PHONE_NUMBER_LENGTH:
                return False

            return True
        except ValueError:
            return False

    def __str__(self):
        return str(self.__number)

    def __repr__(self):
        return str(self)
