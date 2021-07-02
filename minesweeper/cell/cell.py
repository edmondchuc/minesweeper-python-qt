from minesweeper.cell.state.base import CellState
from minesweeper.cell.state.default import CellDefaultState


class Cell:
    def __init__(self, is_bomb: bool = False):
        self.is_bomb = is_bomb
        self._state = CellDefaultState()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: CellState):
        self._state = value

    def set_state_hover_enter(self):
        self._state.set_state_hover_enter(self)

    def set_state_hover_exit(self):
        self._state.set_state_hover_exit(self)

    def set_state_left_click_down(self):
        self._state.set_state_left_click_down(self)

    def set_state_left_click_release(self):
        self._state.set_state_left_click_release(self)
