from typing import TYPE_CHECKING

from minesweeper import settings

if TYPE_CHECKING:
    from minesweeper.cell import Cell

from minesweeper.cell.state.base import CellState
from minesweeper.cell.state.revealed_bomb import CellRevealedBombState
from minesweeper.cell.state.revealed_empty import CellRevealedEmptyState


class CellDownState(CellState):
    image = settings.IMAGE_CELL_DOWN

    def set_state_left_click_release(self, cell: 'Cell'):
        if cell.is_bomb:
            cell.state = CellRevealedBombState()
        else:
            cell.state = CellRevealedEmptyState()
            if cell.neighbour_bomb_count == 1:
                cell.state.image = settings.IMAGE_CELL_REVEALED_ONE
            elif cell.neighbour_bomb_count == 2:
                cell.state.image = settings.IMAGE_CELL_REVEALED_TWO
            elif cell.neighbour_bomb_count == 3:
                cell.state.image = settings.IMAGE_CELL_REVEALED_THREE
            elif cell.neighbour_bomb_count == 4:
                cell.state.image = settings.IMAGE_CELL_REVEALED_FOUR
            elif cell.neighbour_bomb_count == 5:
                cell.state.image = settings.IMAGE_CELL_REVEALED_FIVE
            elif cell.neighbour_bomb_count == 6:
                cell.state.image = settings.IMAGE_CELL_REVEALED_SIX
            elif cell.neighbour_bomb_count == 7:
                cell.state.image = settings.IMAGE_CELL_REVEALED_SEVEN
            elif cell.neighbour_bomb_count == 8:
                cell.state.image = settings.IMAGE_CELL_REVEALED_EIGHT
            # TODO: Determine if any neighbours have bombs or not and reveal neighbours if no bombs.
