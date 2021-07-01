from typing import List

from PySide6.QtWidgets import QBoxLayout, QHBoxLayout

from minesweeper import BoardModel
from minesweeper.cell_view import CellView
from minesweeper.game_controller import GameController


class BoardView:
    cells: List[CellView]

    def __init__(self, rows: int, columns: int, page_layout: QBoxLayout):
        self.board_size = rows * columns
        self.rows = rows
        self.columns = columns
        self.page_layout = page_layout

    def init_view(self, game_controller: GameController):
        self.cells = list()

        identifier = 0
        for i in range(self.rows):
            row_layout = QHBoxLayout()
            row_layout.setSpacing(0)
            for j in range(self.columns):
                cell = CellView(identifier, game_controller)
                self.cells.append(cell)
                identifier += 1
                row_layout.addWidget(cell)
            self.page_layout.addLayout(row_layout)

    def set_view(self, identifier: int, board_model: BoardModel):
        image = board_model.cells[identifier].state.image
        self.cells[identifier].setPixmap(image)
