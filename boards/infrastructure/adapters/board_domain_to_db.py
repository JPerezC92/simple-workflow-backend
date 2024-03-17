from boards.domain.board_model import Board


def board_domain_to_db(board: Board):
    return {
        "id": f"{board.board_id}",
        "title": board.title.value(),
        "created_at": board.created_at.value(),
        "modified_at": board.modified_at.value(),
    }
