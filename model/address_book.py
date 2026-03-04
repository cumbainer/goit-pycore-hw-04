from datetime import date, timedelta
from typing import Optional, List, Dict

from model.record import Record
from utils.constants import BIRTHDAY_GREET_DAYS_AHEAD

CONGRATULATION_DATE_FORMAT = "%d.%m.%Y"


class AddressBook:
    def __init__(self):
        self.__records: List[Record] = []

    def add_record(self, record: Record) -> None:
        self.__records.append(record)

    def find(self, name: str) -> Optional[Record]:
        return next((r for r in self.__records if r.name.name == name), None)

    def delete(self, name: str) -> None:
        record = self.find(name)
        if record:
            self.__records.remove(record)

    @property
    def records(self) -> List[Record]:
        return self.__records

    def get_upcoming_birthdays(self) -> List[Dict[str, str]]:
        today = date.today()
        end_date = today + timedelta(days=BIRTHDAY_GREET_DAYS_AHEAD)
        result: List[Dict[str, str]] = []

        for record in self.__records:
            if record.birthday is None:
                continue

            next_birthday = record.birthday.get_next_birthday()
            if not (today <= next_birthday <= end_date):
                continue

            congrat = next_birthday
            if congrat.weekday() == 5:
                congrat += timedelta(days=2)
            elif congrat.weekday() == 6:
                congrat += timedelta(days=1)

            result.append({
                "name": record.name.name,
                "congratulation_date": congrat.strftime(CONGRATULATION_DATE_FORMAT),
            })

        return result

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.__records)
