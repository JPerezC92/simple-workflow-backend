from typing import Callable, Generic
from uuid import UUID

from boards.domain.board_model import Board
from boards.domain.board_not_found_exception import BoardNotFoundException
from boards.domain.board_repository import BoardRepository
from shared.application.use_case_output import UseCaseOutput


class BoardFinder(Generic[UseCaseOutput]):
    def __init__(
        self,
        board_repository: BoardRepository,
        output_adapter: Callable[[Board], UseCaseOutput],
    ):
        self.board_repository = board_repository
        self.output_adapter = output_adapter

    async def execute(self, board_id: UUID):
        board = await self.board_repository.find_board(board_id)

        if board is None:
            return BoardNotFoundException(board_id=board_id)

        return self.output_adapter(board)
