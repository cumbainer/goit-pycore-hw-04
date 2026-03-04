from model.fields.base_field import Field


class Name(Field):
    def __init__(self, value: str):
        super().__init__("name", value)
        self.__name = value

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self):
        return self.name
