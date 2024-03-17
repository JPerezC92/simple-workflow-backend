from abc import ABC, ABCMeta
from uuid import UUID

from boards.domain.board_model import Board


class AbstractRepository(ABC):
    pass


class BoardRepository(metaclass=ABCMeta):
    async def create_board(self, board: Board) -> Board:  # type: ignore
        pass

    async def find_board(self, board_id: UUID) -> Board | None:
        pass

    async def update_board(self, board: Board):
        pass
