from random import randrange
from typing import Set, List

from minesweeper.cell import Cell
from minesweeper.cell.state.default import CellDefaultState
from minesweeper.cell.state.down import CellDownState
from minesweeper.cell.state.revealed_bomb import CellRevealedBombState
from minesweeper.cell.state.revealed_empty import CellRevealedEmptyState


class BoardModel:

    def _get_bomb_cell_identifiers(self) -> Set[int]:
        bomb_cell_identifiers = set()
        for i in range(self.bomb_count):
            while True:
                identifier = randrange(self.board_size)
                if identifier not in bomb_cell_identifiers:
                    bomb_cell_identifiers.add(identifier)
                    break
        return bomb_cell_identifiers

    def _create_cells(self, bomb_cell_identifiers: Set[int]) -> List[Cell]:
        cells = [
            Cell(
                identifier,
                True if identifier in bomb_cell_identifiers else False
            )
            for identifier in range(self.board_size)
        ]

        return cells

    def _get_cell_neighbour_identifiers(self, identifier: int) -> List[Cell]:
        neighbour_cells = list()

        top_left_cell = identifier - self.board_length - 1
        if top_left_cell >= 0 and identifier % self.board_length != 0:
            neighbour_cells.append(self.cells[top_left_cell])

        top_cell = identifier - self.board_length
        if top_cell >= 0:
            neighbour_cells.append(self.cells[top_cell])

        top_right_cell = identifier - self.board_length + 1
        if top_right_cell > 0 and identifier % self.board_length != self.board_length - 1:
            neighbour_cells.append(self.cells[top_right_cell])

        left_cell = identifier - 1
        if identifier % self.board_length != 0:
            neighbour_cells.append(self.cells[left_cell])

        right_cell = identifier + 1
        if identifier % self.board_length != self.board_length - 1:
            neighbour_cells.append(self.cells[right_cell])

        bottom_left_cell = identifier + self.board_length - 1
        if bottom_left_cell < self.board_size and identifier % self.board_length != 0:
            neighbour_cells.append(self.cells[bottom_left_cell])

        bottom_cell = identifier + self.board_length
        if bottom_cell < self.board_size:
            neighbour_cells.append(self.cells[bottom_cell])

        bottom_right_cell = identifier + self.board_length + 1
        if bottom_right_cell < self.board_size and identifier % self.board_length != self.board_length - 1:
            neighbour_cells.append(self.cells[bottom_right_cell])

        return neighbour_cells

    def __init__(self, board_length: int, bomb_count: int):
        self.board_length = board_length
        self.board_size = board_length * board_length
        self.bomb_count = bomb_count

        bomb_cell_identifiers = self._get_bomb_cell_identifiers()
        self.cells = self._create_cells(bomb_cell_identifiers)

        for identifier, cell in enumerate(self.cells):
            # Set neighbours
            cell.neighbours = self._get_cell_neighbour_identifiers(identifier)

            # Set cell neighbour count with bombs
            for neighbour in cell.neighbours:
                if neighbour.is_bomb:
                    cell.neighbour_bomb_count += 1

    def cell_hover_enter_event(self, identifier: int):
        self.cells[identifier].set_state_hover_enter()

    def cell_hover_leave_event(self, identifier: int):
        self.cells[identifier].set_state_hover_exit()

    def cell_left_click_down_event(self, identifier: int):
        self.cells[identifier].set_state_left_click_down()

    def reveal_neighbours(self, cell: Cell):
        if cell.neighbour_bomb_count == 0:
            for neighbour in cell.neighbours:
                if isinstance(neighbour.state, CellDefaultState):
                    neighbour.state = CellDownState()
                    neighbour.set_state_left_click_release()
                    if neighbour.neighbour_bomb_count == 0:
                        self.reveal_neighbours(neighbour)

    def cell_left_click_release_event(self, identifier: int):
        cell = self.cells[identifier]
        current_state = cell.state
        cell.set_state_left_click_release()

        if current_state != cell.state:
            self.reveal_neighbours(cell)
