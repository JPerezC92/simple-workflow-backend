from typing import Callable, Generic
from uuid import UUID

from boards.domain.board_model import Board
from boards.domain.board_not_found_exception import BoardNotFoundException
from boards.domain.board_repository import BoardRepository
from shared.application.use_case_output import UseCaseOutput


class BoardUpdater(Generic[UseCaseOutput]):
    def __init__(
        self,
        board_repository: BoardRepository,
        output_adapter: Callable[[Board], UseCaseOutput],
    ):
        self.board_repository = board_repository
        self.output_adapter = output_adapter

    async def execute(self, board_id: UUID, title: str):
        board_found = await self.board_repository.find_board(board_id)

        if board_found is None:
            return BoardNotFoundException(board_id=board_id)

        board_found = board_found.change_title(title)

        await self.board_repository.update_board(board_found)

        return self.output_adapter(board_found)
