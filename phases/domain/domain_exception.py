from abc import ABC, abstractmethod


class DomainException(ABC, Exception):
    @property
    @abstractmethod
    def error_code(self) -> str:
        pass

    @property
    @abstractmethod
    def message(self) -> str:
        pass
