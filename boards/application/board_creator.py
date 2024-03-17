from typing import Callable, Generic

from boards.domain.board_model import Board
from boards.domain.board_repository import BoardRepository
from boards.domain.title import Title
from phases.application.phase_updater import UseCaseOutput


class BoardCreator(Generic[UseCaseOutput]):
    def __init__(
        self,
        board_repository: BoardRepository,
        output_adapter: Callable[[Board], UseCaseOutput],
    ):
        self.board_repository = board_repository
        self.output_adapter = output_adapter

    async def execute(self, title: str):

        newBoard = Board.create(title=Title(title))

        board = await self.board_repository.create_board(newBoard)

        return self.output_adapter(board)
