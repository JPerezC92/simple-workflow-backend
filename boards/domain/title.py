class Title:
    _value: str

    def __init__(self, value: str):
        if len(value) < 3:
            raise ValueError("Title must be at least 3 characters long")
        self._value = value

    def change(self, new_title: str):
        return Title(new_title)

    def value(self):
        return self._value