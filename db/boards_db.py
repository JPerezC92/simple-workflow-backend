# type: ignore
from uuid import UUID

from tortoise import fields, models


class BoardsDB(models.Model):
    id: UUID = fields.data.UUIDField(pk=True)
    title = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "boards"
