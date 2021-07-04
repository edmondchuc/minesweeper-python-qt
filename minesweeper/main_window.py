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
        page_layout.setSpacing(0)
        page_layout.setSizeConstraint(page_layout.SetFixedSize)
        self.centralWidget().setLayout(page_layout)

        title_label = QLabel('Welcome!')
        page_layout.addWidget(title_label)

        rows = 9
        columns = 9
        board_length = 9
        bomb_count = 10
        board_size = rows * columns
        board_model = BoardModel(board_length, bomb_count)
        board_view = BoardView(rows, columns, page_layout)
        game_controller = GameController(board_model, board_view)
