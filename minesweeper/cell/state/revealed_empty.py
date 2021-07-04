from minesweeper import settings
from minesweeper.cell.state.base import CellState


class CellRevealedEmptyState(CellState):
    image = settings.IMAGE_CELL_REVEALED_EMPTY
