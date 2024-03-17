from typing import Callable, Generic
from uuid import UUID

from phases.domain.phase_model import Phase
from phases.domain.phase_not_found_exception import PhaseNotFoundException
from phases.domain.phase_repository import PhaseRepository
from shared.application.use_case_output import UseCaseOutput


class PhaseFinder(Generic[UseCaseOutput]):
    def __init__(
        self,
        phase_repository: PhaseRepository,
        output_adapter: Callable[[Phase], UseCaseOutput],
    ):
        self.phase_repository = phase_repository
        self.output_adapter = output_adapter

    async def execute(self, phase_id: UUID):
        phase = await self.phase_repository.find_phase_by_id(phase_id)

        if not phase:
            return PhaseNotFoundException(phase_id)

        return self.output_adapter(phase)
