from boards.domain.board_model import Board
from boards.infrastructure.schemas.board_schema import BoardSchema


def board_model_to_endpoint(board: Board):
    return BoardSchema(
        id=board.board_id,
        title=board.title.value(),
        created_at=board.created_at.value(),
        modified_at=board.modified_at.value(),
    )
