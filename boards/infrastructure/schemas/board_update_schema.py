from typing import Annotated

from pydantic import Field

from boards.infrastructure.schemas.board_create_schema import BoardCreate


class BoardUpdate(BoardCreate):
    title: Annotated[str, Field(description="A title for the board", max_length=50)]


BoardUpdateSchema = BoardUpdate
