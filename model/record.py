from typing import List, Optional

from model.name_field import NameField
from model.phone_field import PhoneField


class Record:
    def __init__(self, name: str, phone_numbers_param: Optional[List[int]] = None):
        self.__name = NameField(name)
        self.__phone_numbers: List[PhoneField] = [] if phone_numbers_param is None else list(
            map(PhoneField, phone_numbers_param))

    def add_phone(self, phone_number_param: int) -> PhoneField:
        phone_number = PhoneField(phone_number_param)
        self.__phone_numbers.append(phone_number)

        print(f"Added {phone_number_param} to {self.__phone_numbers}")
        return phone_number

    def remove_phone(self, phone_number_param: int) -> PhoneField:
        phone_number = PhoneField(phone_number_param)
        self.__phone_numbers.remove(phone_number)

        print(f"Removed {phone_number_param}")
        return phone_number

    def edit_phone(self, old_number_param: int, new_number_param: int) -> PhoneField:
        old_number_to_remove = next(n for n in self.__phone_numbers if n.number == old_number_param)
        new_number = PhoneField(new_number_param)

        self.__phone_numbers.remove(old_number_to_remove)
        self.__phone_numbers.append(new_number)

        print(f"Edited {old_number_param} to {new_number_param}")
        return new_number

    def find_phone(self, name: str) -> Optional[PhoneField]:
        name_field = NameField(name)

        return next((number for number in self.__phone_numbers if self.__name == name_field), None)

    @property
    def name(self) -> str:
        return self.__name.name

    @property
    def phone_numbers(self) -> List[PhoneField]:
        return self.__phone_numbers

    def __str__(self) -> str:
        return f"Name: {self.name}, Phone Numbers: {self.phone_numbers}"


    def __repr__(self) -> str:
        return str(self)