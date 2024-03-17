from uuid import UUID

from db.phases_db import PhasesDB
from phases.domain.phase_model import Phase
from phases.domain.phase_repository import PhaseRepository
from phases.infrastructure.adapters.phase_db_to_domain import \
    phase_db_to_domain


class PhaseProdRepository(PhaseRepository):
    async def find_phases(self) -> list[Phase]:
        phases_db_list = await PhasesDB.all()

        return [phase_db_to_domain(phase) for phase in phases_db_list]

    async def find_phase_by_id(self, phase_id: UUID) -> Phase | None:
        phase_db = await PhasesDB.get_or_none(id=phase_id)

        if not phase_db:
            return None

        return phase_db_to_domain(phase_db)

    async def add_phase(self, phase: Phase) -> None:
        print("add_phase")
        await PhasesDB.create(
            id=phase.phase_id,
            title=phase.title,
            description=phase.description,
            order=phase.order,
            board_id=phase.board_id,
        )

    async def update_phase(self, phase: Phase) -> None:
        await PhasesDB.filter(id=phase.phase_id).update(
            title=phase.title,
            description=phase.description,
        )
