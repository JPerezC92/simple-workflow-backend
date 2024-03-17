from uuid import UUID

from boards.domain.board_not_found_exception import BoardNotFoundException
from boards.domain.board_repository import BoardRepository
from phases.domain.phase_model import Phase
from phases.domain.phase_repository import PhaseRepository


class PhaseCreator:
    def __init__(
        self, phase_repository: PhaseRepository, board_repository: BoardRepository
    ):
        self.phase_repository = phase_repository
        self.board_repository = board_repository

    async def execute(self, phase_title: str, phase_description: str, board_id: UUID):
        board = await self.board_repository.find_board(board_id)
        if not board:
            return BoardNotFoundException(board_id)

        new_phase = Phase.create(phase_title, phase_description, 0, board.board_id)
        print("PhaseCreator")

        await self.phase_repository.add_phase(new_phase)
