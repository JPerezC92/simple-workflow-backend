from uuid import UUID

from phases.domain.domain_exception import DomainException


class PhaseNotFoundException(DomainException):
    id_not_found: UUID

    def __init__(self, phase_id: UUID):
        self.id_not_found = phase_id

    @property
    def error_code(self):
        return "phase_not_found"

    @property
    def message(self) -> str:
        if self.id_not_found:
            return f"Phase with id {self.id_not_found} not found"

        return "Phase not found"
