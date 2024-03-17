from typing import Annotated

from pydantic import BaseModel, Field


class BoardCreate(BaseModel):
    title: Annotated[str, Field(description="A title for the board", max_length=50)]


BoardCreateSchema = BoardCreate
