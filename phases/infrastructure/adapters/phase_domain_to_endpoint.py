from phases.domain.phase_model import Phase
from phases.infrastructure.schemas.phase_schema import PhaseSchema


def phase_domain_to_endpoint(phase: Phase):
    return PhaseSchema(
        id=phase.phase_id,
        title=phase.title,
        description=phase.description,
        board_id=phase.board_id,
        created_at=phase.created_at,
        modified_at=phase.modified_at,
    )



def phase_endpoint_to_domain_list(phase_list: list[Phase]):
    return [phase_domain_to_endpoint(phase) for phase in phase_list]
