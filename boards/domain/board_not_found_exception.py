from uuid import UUID

from phases.domain.domain_exception import DomainException


class BoardNotFoundException(DomainException):
    id_not_found: UUID

    def __init__(self, board_id: UUID):
        self.id_not_found = board_id

    @property
    def error_code(self):
        return "board_not_found"

    @property
    def message(self) -> str:
        if self.id_not_found:
            return f"Board with id {self.id_not_found} not found"

        return "Board not found"
