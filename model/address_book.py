from typing import Optional, List

from model.record import Record


class AddressBook:
    def __init__(self, init_records: Optional[List[Record]] = None):
        self.__records = [] if init_records is None else init_records

    def add_record(self, record: Record) -> Record:
        self.__records.append(record)

        print(f"Record {record} added to {self.__records}")
        return record

    def find_record(self, name: str) -> Optional[Record]:
        return next((record for record in self.__records if record.name == name), None)

    def delete_record(self, name: str) -> Record | None:
        record = next((record for record in self.__records if record.name == name), None)
        if not record:
            return None
        self.__records.remove(record)

        print(f"Record {record.name} deleted")
        return record

    @property
    def records(self) -> List[Record]:
        return self.__records

    def __str__(self):
        return str(self.__dict__)
