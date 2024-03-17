from datetime import datetime
from typing import Any
from uuid import UUID, uuid4


class Phase:
    def __init__(
        self,
        phase_id: UUID,
        title: str,
        description: str,
        order: int,
        created_at: datetime,
        modified_at: datetime,
        board_id: UUID,
    ):
        self.phase_id = phase_id
        self.title = title
        self.description = description
        self.order = order
        self.created_at = created_at
        self.modified_at = modified_at
        self.board_id = board_id

    @staticmethod
    def create(title: str, description: str, order: int, board_id: UUID):
        return Phase(
            phase_id=uuid4(),
            title=title,
            description=description,
            order=order,
            created_at=datetime.now(),
            modified_at=datetime.now(),
            board_id=board_id,
        )

    def change_title(self, title: str | None = None):
        update: dict[str, Any] = {
            **self.__dict__,
            "title": title or self.title,
            "modified_at": datetime.now(),
        }
        return Phase(**update)

    def change_description(self, description: str | None = None):
        print("change_description")
        update: dict[str, Any] = {
            **self.__dict__,
            "description": description or self.description,
            "modified_at": datetime.now(),
        }

        return Phase(**update)
