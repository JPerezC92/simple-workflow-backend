from uuid import UUID

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class PhaseCreate(BaseModel):
    title: Annotated[str, Field(description="A title for the phase", max_length=50)]
    description: Annotated[
        str, Field(description="A description for the phase", max_length=250)
    ]
    board_id: Annotated[UUID, Field(description="The board id this phase belongs to")]


PhaseCreateSchema = PhaseCreate
