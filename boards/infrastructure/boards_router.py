from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from tortoise.transactions import atomic

from boards.application.board_creator import BoardCreator
from boards.application.board_finder import BoardFinder
from boards.application.board_updater import BoardUpdater
from boards.domain.board_not_found_exception import BoardNotFoundException
from boards.infrastructure.adapters.board_model_to_endpoint import \
    board_model_to_endpoint
from boards.infrastructure.schemas.board_create_schema import BoardCreateSchema
from boards.infrastructure.schemas.board_schema import BoardSchema
from boards.infrastructure.schemas.board_update_schema import BoardUpdateSchema
from boards.infrastructure.services.board_prod_repository import \
    BoardProdRepository
from shared.infrastructure.decorators.controller import controller
from shared.infrastructure.responses.not_found_response import NotFoundResponse

boards_router = APIRouter(prefix="/boards", tags=["boards"])


@boards_router.post(
    "/",
    response_model=BoardSchema,
)
@atomic()
@controller()
async def create_board(board_create_schema: BoardCreateSchema):
    new_board = await BoardCreator(
        board_repository=BoardProdRepository(),
        output_adapter=board_model_to_endpoint,
    ).execute(board_create_schema.title)

    return new_board


@boards_router.get("/{board_id}")
@atomic()
@controller()
async def find_board(board_id: UUID):
    result = await BoardFinder(
        board_repository=BoardProdRepository(), output_adapter=board_model_to_endpoint
    ).execute(board_id)

    match result:
        case BoardNotFoundException():
            return JSONResponse(
                status_code=NotFoundResponse.status_code(),
                content=NotFoundResponse.get_content(result),
            )
        case BoardSchema():
            return result


@boards_router.put("/{board_id}")
@atomic()
@controller()
async def update_board(board_id: UUID, board_update: BoardUpdateSchema):
    result = await BoardUpdater(BoardProdRepository(), board_model_to_endpoint).execute(
        board_id, board_update.title
    )

    match result:
        case BoardNotFoundException():
            return JSONResponse(
                status_code=NotFoundResponse.status_code(),
                content=NotFoundResponse.get_content(result),
            )
        case BoardSchema():
            return result
