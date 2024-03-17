# type: ignore
from uuid import UUID

from tortoise import fields, models

from db.boards_db import BoardsDB


class PhasesDB(models.Model):
    id: UUID = fields.data.UUIDField(pk=True)
    title = fields.CharField(max_length=100)
    description = fields.TextField()
    order = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now_add=True)
    board_id: UUID

    board: fields.ForeignKeyRelation[BoardsDB] = fields.ForeignKeyField(
        "models.BoardsDB",
        related_name="phases",
        description="The board this phase belongs to",
    )

    class Meta:
        table = "phases"
