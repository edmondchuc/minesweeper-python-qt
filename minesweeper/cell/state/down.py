from typing import TYPE_CHECKING

from minesweeper import settings

if TYPE_CHECKING:
    from minesweeper.cell import Cell

from minesweeper.cell.state.base import CellState
from minesweeper.cell.state.revealed_bomb import CellRevealedBomb
from minesweeper.cell.state.revealed_empty import CellRevealedEmpty


class CellDownState(CellState):
    image = settings.IMAGE_CELL_DOWN

    def set_state_left_click_release(self, cell: 'Cell'):
        if cell.is_bomb:
            cell.state = CellRevealedBomb()
        else:
            cell.state = CellRevealedEmpty()
            # TODO: Determine if any neighbours have bombs or not and reveal neighbours if no bombs.
