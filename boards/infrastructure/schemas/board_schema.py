from typing import Annotated
from uuid import UUID

from pydantic import Field

from boards.infrastructure.schemas.board_create_schema import BoardCreate
from shared.infrastructure.schemas.timestamp_schema import Timestamp


class Board(BoardCreate, Timestamp):
    id: Annotated[UUID, Field(description="The board unique identifier")]


BoardSchema = Board
