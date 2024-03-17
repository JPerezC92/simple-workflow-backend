from abc import ABC, abstractmethod
from uuid import UUID

from phases.domain.phase_model import Phase


class PhaseRepository(ABC):
    @abstractmethod
    async def add_phase(self, phase: Phase) -> None:
        pass
    

    @abstractmethod
    async def update_phase(self, phase: Phase) -> None:
        pass

    @abstractmethod
    async def find_phases(self) -> list[Phase]:
        pass

    @abstractmethod
    async def find_phase_by_id(self, phase_id: UUID) -> Phase | None:
        pass
