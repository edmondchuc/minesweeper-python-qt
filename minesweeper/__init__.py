from typing import Callable

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from minesweeper.board_model import BoardModel
from minesweeper import settings
from minesweeper.board_view import BoardView
from minesweeper.game_controller import GameController


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(settings.TITLE)
        container = QWidget()
        self.setCentralWidget(container)

        page_layout = QVBoxLayout()
        self.centralWidget().setLayout(page_layout)
        title_label = QLabel('Welcome!')
        page_layout.addWidget(title_label)

        rows = 3
        columns = 3
        board_size = rows * columns
        board_model = BoardModel(board_size)
        board_view = BoardView(rows, columns, page_layout)
        game_controller = GameController(board_model, board_view)

        page_layout.setSpacing(0)
        page_layout.setSizeConstraint(page_layout.SetFixedSize)

    def cell_click_handler(self, x: int, y: int):
        print(f'x: {x}, y: {y}')
