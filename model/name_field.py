from model.base_field import Field


NAME_FIELD_ID = "name"
class NameField(Field):
    def __init__(self, value: str):
        super().__init__(NAME_FIELD_ID, value)
        self.__name = value

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self):
        return self.name
