from PySide6.QtCore import QEvent
from PySide6.QtGui import QPixmap, QMouseEvent, Qt, QEnterEvent
from PySide6.QtWidgets import QLabel

from minesweeper import settings
from minesweeper.game_controller import GameController


class CellView(QLabel):
    image_default = settings.IMAGE_CELL_DEFAULT

    def __init__(self, identifier: int, game_controller: GameController):
        super(CellView, self).__init__()

        self.identifier = identifier
        self.game_controller = game_controller

        self.setPixmap(self.image_default)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        if ev.button() == Qt.LeftButton:
            print(f'x: {self.x}, y: {self.y} - left button pressed')
        elif ev.button() == Qt.RightButton:
            print(f'x: {self.x}, y: {self.y} - right button pressed')

    def enterEvent(self, event: QEnterEvent) -> None:
        self.game_controller.cell_hover_enter_event(self.identifier)

    def leaveEvent(self, event: QEvent) -> None:
        self.game_controller.cell_hover_leave_event(self.identifier)
