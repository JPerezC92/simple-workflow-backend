from boards.domain.board_model import Board
from boards.domain.title import Title
from db.boards_db import BoardsDB
from shared.domain.timestamp import Timestamp


def board_db_to_domain(board_db: BoardsDB) -> Board:
    return Board(
        board_id=board_db.id, 
        title=Title(board_db.title),
        created_at=Timestamp(board_db.created_at),
        modified_at=Timestamp(board_db.modified_at),
    )
