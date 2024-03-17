from typing import Annotated

from pydantic import UUID4, Field

from phases.infrastructure.schemas.phase_create_schema import PhaseCreate
from shared.infrastructure.schemas.timestamp_schema import Timestamp


class Phase(PhaseCreate, Timestamp):
    id: Annotated[UUID4, Field(description="The identifier assigned to the phase")]


PhaseSchema = Phase
