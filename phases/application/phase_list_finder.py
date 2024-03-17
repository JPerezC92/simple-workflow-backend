from typing import Callable, Generic

from phases.domain.phase_model import Phase
from phases.domain.phase_repository import PhaseRepository
from shared.application.use_case_output import UseCaseOutput


class PhaseListFinder(Generic[UseCaseOutput]):
    def __init__(
        self,
        phase_repository: PhaseRepository,
        output_adapter: Callable[[list[Phase]], UseCaseOutput],
    ):
        self.phase_repository = phase_repository
        self.output_adapter = output_adapter

    async def execute(self) -> UseCaseOutput:
        phases = await self.phase_repository.find_phases()
        return self.output_adapter(phases)
