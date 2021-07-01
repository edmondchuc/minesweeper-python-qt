from typing import Callable

from PySide6.QtGui import QPixmap, QMouseEvent, Qt, QEnterEvent
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from minesweeper import settings


class Cell(QLabel):
    """Cell

    A cell has the following states.
    - default
    - hover

    States.
    default -> hover
    hover -> default
    """
    image_default = settings.IMAGE_CELL_DEFAULT

    def __init__(self, x: int, y: int, mouse_click_callback: Callable[[int, int], None]):
        super(Cell, self).__init__()

        self.x = x
        self.y = y
        cell_pixmap = QPixmap(self.image_default)
        self.setPixmap(cell_pixmap)
        self.mouse_click_callback = mouse_click_callback

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            self.mouse_click_callback(self.x, self.y)
        elif ev.button() == Qt.RightButton:
            print(f'x: {self.x}, y: {self.y} - right button pressed')

    def enterEvent(self, event: QEnterEvent) -> None:
        print(event.type())


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

        for i in range(rows):
            row_layout = QHBoxLayout()
            row_layout.setSpacing(0)
            for j in range(columns):
                cell = Cell(i, j, self.cell_click_handler)
                row_layout.addWidget(cell)
            page_layout.addLayout(row_layout)

        page_layout.setSpacing(0)
        page_layout.setSizeConstraint(page_layout.SetFixedSize)

    def cell_click_handler(self, x: int, y: int):
        print(f'x: {x}, y: {y}')
