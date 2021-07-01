from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from minesweeper.cell import Cell


class CellState:
    image: str

    def set_state_hover_enter(self, cell: 'Cell'):
        pass

    def set_state_hover_exit(self, cell: 'Cell'):
        pass

    def set_state_left_click(self, cell: 'Cell'):
        pass

    def set_state_right_click(self, cell: 'Cell'):
        pass

    def set_state_reveal_empty(self, cell: 'Cell'):
        pass

    def set_state_reveal_bomb(self, cell: 'Cell'):
        pass
