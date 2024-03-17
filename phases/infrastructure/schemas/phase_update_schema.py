from pydantic import BaseModel, Field
from typing_extensions import Annotated


class PhaseUpdate(BaseModel):
    title: (
        Annotated[
            str,
            Field(description="The new title of the phase", max_length=50),
        ]
        | None
    ) = None

    description: (
        Annotated[
            str,
            Field(description="The new description of the phase", max_length=250),
        ]
        | None
    ) = None


PhaseUpdateSchema = PhaseUpdate
