from typing import List, Optional

from model.fields.birthday_field import Birthday
from model.fields.name_field import Name
from model.fields.phone_field import Phone


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Optional[Birthday] = None

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        self.phones.remove(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone: str) -> Optional[Phone]:
        return next((p for p in self.phones if p.number == phone), None)

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        phones = "; ".join(str(p) for p in self.phones)
        result = f"Contact name: {self.name}, phones: {phones}"
        if self.birthday:
            result += f", birthday: {self.birthday.value}"
        return result

    def __repr__(self) -> str:
        return str(self)
