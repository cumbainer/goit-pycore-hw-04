from abc import ABC


class Field(ABC):

    def __init__(self, field_id: str, value: str):
        self.field_id = field_id
        self.value = value


