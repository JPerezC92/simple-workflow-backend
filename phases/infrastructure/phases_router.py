from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from tortoise.transactions import atomic

from boards.domain.board_not_found_exception import BoardNotFoundException
from boards.infrastructure.services.board_prod_repository import \
    BoardProdRepository
from phases.application.phase_creator import PhaseCreator
from phases.application.phase_finder import PhaseFinder
from phases.application.phase_list_finder import PhaseListFinder
from phases.application.phase_updater import PhaseUpdater
from phases.domain.phase_not_found_exception import PhaseNotFoundException
from phases.infrastructure.adapters.phase_domain_to_endpoint import (
    phase_domain_to_endpoint, phase_endpoint_to_domain_list)
from phases.infrastructure.schemas.phase_create_schema import PhaseCreateSchema
from phases.infrastructure.schemas.phase_schema import PhaseSchema
from phases.infrastructure.schemas.phase_update_schema import PhaseUpdateSchema
from phases.infrastructure.services.phase_prod_repository import \
    PhaseProdRepository
from shared.infrastructure.decorators.controller import controller
from shared.infrastructure.responses.not_found_response import NotFoundResponse

phases_router = APIRouter(prefix="/phases", tags=["phases"])


@phases_router.get("/", response_model=List[PhaseSchema])
@atomic()
@controller()
async def find_all_phases():
    return await PhaseListFinder(
        phase_repository=PhaseProdRepository(),
        output_adapter=phase_endpoint_to_domain_list,
    ).execute()


@phases_router.get(
    "/{phase_id}",
    response_model=PhaseSchema,
    responses={NotFoundResponse.status_code(): {"model": NotFoundResponse}},
)
@atomic()
@controller()
async def find_phase(phase_id: UUID):
    result = await PhaseFinder(
        phase_repository=PhaseProdRepository(), output_adapter=phase_domain_to_endpoint
    ).execute(phase_id)

    match result:
        case PhaseNotFoundException():
            return JSONResponse(
                status_code=NotFoundResponse.status_code(),
                content=NotFoundResponse.get_content(result),
            )
        case PhaseSchema():
            return result


@phases_router.post("", response_model=Annotated[None, None], status_code=201)
@atomic()
@controller()
async def create_phase(phase_create_schema: PhaseCreateSchema):
    result = await PhaseCreator(
        phase_repository=PhaseProdRepository(), board_repository=BoardProdRepository()
    ).execute(
        phase_title=phase_create_schema.title,
        phase_description=phase_create_schema.description,
        board_id=phase_create_schema.board_id,
    )

    match result:
        case BoardNotFoundException():
            return JSONResponse(
                status_code=NotFoundResponse.status_code(),
                content=NotFoundResponse.get_content(result),
            )
        case None:
            return None


@phases_router.put(
    "/{phase_id}",
    response_model=PhaseSchema,
    responses={NotFoundResponse.status_code(): {"model": NotFoundResponse}},
)
@atomic()
@controller()
async def update_phase(phase_id: UUID, phase_update: PhaseUpdateSchema):
    result = await PhaseUpdater(
        phase_repository=PhaseProdRepository(), output_adapter=phase_domain_to_endpoint
    ).execute(
        phase_id=phase_id,
        phase_title=phase_update.title,
        phase_description=phase_update.description,
    )

    match result:
        case PhaseNotFoundException():
            return JSONResponse(
                status_code=NotFoundResponse.status_code(),
                content=NotFoundResponse.get_content(result),
            )
        case PhaseSchema():
            return result
