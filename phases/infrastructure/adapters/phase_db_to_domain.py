from db.phases_db import PhasesDB
from phases.domain.phase_model import Phase


def phase_db_to_domain(phase_db: PhasesDB) -> Phase:
    return Phase(
        phase_db.id,
        phase_db.title,
        phase_db.description,
        phase_db.order,
        phase_db.created_at,
        phase_db.modified_at,
        phase_db.board_id,
    )
