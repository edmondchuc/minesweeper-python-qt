from typing import List

from minesweeper.cell.state.base import CellState
from minesweeper.cell.state.default import CellDefaultState


class Cell:

    def __init__(self, identifier: int, is_bomb: bool = False):
        self._identifier = identifier
        self.is_bomb = is_bomb
        self._state = CellDefaultState()
        self._neighbours = list()
        self.neighbour_bomb_count = 0

    def __repr__(self):
        return f'Cell {self.identifier}'

    @property
    def identifier(self):
        return self._identifier

    @property
    def neighbours(self) -> List['Cell']:
        return self._neighbours

    @neighbours.setter
    def neighbours(self, value: List['Cell']):
        self._neighbours = value

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
