from datetime import datetime


class Timestamp:
    _value: datetime

    def __init__(self, created_at: datetime):
        self._value = created_at

    def value(self):
        return self._value

    def change(self, new_created_at: datetime):
        return Timestamp(new_created_at)
