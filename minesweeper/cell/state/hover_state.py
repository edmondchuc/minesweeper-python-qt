from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from minesweeper.cell import Cell
from minesweeper.cell.state.base_state import CellState

from minesweeper import settings


class CellHoverState(CellState):
    image = settings.IMAGE_CELL_HOVER

    def __init__(self, previous_state: CellState):
        self.previous_state = previous_state

    def set_state_hover_exit(self, cell: 'Cell'):
        cell.state = self.previous_state
