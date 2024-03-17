from datetime import datetime
from uuid import UUID, uuid4

from boards.domain.title import Title
from shared.domain.timestamp import Timestamp


class Board:

    def __init__(
        self,
        board_id: UUID,
        title: Title,
        created_at: Timestamp,
        modified_at: Timestamp,
    ):
        self.board_id = board_id
        self.title = title
        self.created_at = created_at
        self.modified_at = modified_at

    def change_title(self, new_title: str):
        return Board(
            board_id=self.board_id,
            title=self.title.change(new_title),
            created_at=self.created_at,
            modified_at=self.modified_at.change(datetime.now()),
        )

    @staticmethod
    def create(title: Title):
        return Board(
            board_id=uuid4(),
            title=title,
            created_at=Timestamp(datetime.now()),
            modified_at=Timestamp(datetime.now()),
        )
