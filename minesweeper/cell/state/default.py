from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from minesweeper.cell import Cell
from minesweeper.cell.state.base import CellState
from minesweeper.cell.state.hover import CellHoverState

from minesweeper import settings


class CellDefaultState(CellState):
    image = settings.IMAGE_CELL_DEFAULT

    def set_state_hover_enter(self, cell: 'Cell'):
        cell.state = CellHoverState(cell.state)
