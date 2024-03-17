from uuid import UUID

from boards.domain.board_model import Board
from boards.domain.board_repository import BoardRepository
from boards.infrastructure.adapters.board_domain_to_db import \
    board_domain_to_db
from boards.infrastructure.services.board_db_to_domain import \
    board_db_to_domain
from db.boards_db import BoardsDB


class BoardProdRepository(BoardRepository):
    async def create_board(self, board: Board) -> Board:
        # raise NotImplementedError
        await BoardsDB.create(using_db=None, **board_domain_to_db(board))

        return board

    async def find_board(self, board_id: UUID) -> Board | None:

        board = await BoardsDB.get_or_none(id=board_id)

        if board is None:
            return None

        return board_db_to_domain(board)

    async def update_board(self, board: Board):
        board_db = board_domain_to_db(board)
        board_db.pop("id")
        await BoardsDB.filter(id=board.board_id).update(**board_db)
