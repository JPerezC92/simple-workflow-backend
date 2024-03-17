from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class Timestamp(BaseModel):
    created_at: Annotated[
        datetime,
        Field(
            # default_factory=datetime.now,
            description="The date and time the record was created",
        ),
    ]
    modified_at: Annotated[
        datetime,
        Field(
            # default_factory=datetime.now,
            description="The date and time the record was last updated",
        ),
    ]


TimestampSchema = Timestamp
