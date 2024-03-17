from typing import Callable, Generic
from uuid import UUID

from phases.domain.phase_model import Phase
from phases.domain.phase_not_found_exception import PhaseNotFoundException
from phases.domain.phase_repository import PhaseRepository
from shared.application.use_case_output import UseCaseOutput


class PhaseUpdater(Generic[UseCaseOutput]):
    def __init__(
        self,
        phase_repository: PhaseRepository,
        output_adapter: Callable[[Phase], UseCaseOutput],
    ):
        self.phase_repository = phase_repository
        self.output_adapter = output_adapter

    async def execute(
        self,
        phase_id: UUID,
        phase_title: str | None = None,
        phase_description: str | None = None,
    ):
        phase_found = await self.phase_repository.find_phase_by_id(phase_id)

        if not phase_found:
            return PhaseNotFoundException(phase_id)

        phase_updated = phase_found.change_title(phase_title).change_description(
            phase_description
        )
        print("phase_updated")

        await self.phase_repository.update_phase(phase_updated)
        return self.output_adapter(phase_updated)
