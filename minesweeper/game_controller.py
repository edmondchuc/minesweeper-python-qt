from typing import TYPE_CHECKING

from minesweeper.board_model import BoardModel

if TYPE_CHECKING:
    from minesweeper.board_view import BoardView


class GameController:
    def __init__(self, board_model: BoardModel, board_view: 'BoardView'):
        self.board_model = board_model
        self.view = board_view

        board_view.init_view(self)
        self.board_view = board_view

    def cell_hover_enter_event(self, identifier: int):
        self.board_model.cell_hover_enter_event(identifier)
        self.view.set_view(identifier, self.board_model)

    def cell_hover_leave_event(self, identifier: int):
        self.board_model.cell_hover_leave_event(identifier)
        self.view.set_view(identifier, self.board_model)

    def cell_left_click_down_event(self, identifier: int):
        self.board_model.cell_left_click_down_event(identifier)
        self.view.set_view(identifier, self.board_model)

    def cell_left_click_release_event(self, identifier: int):
        self.board_model.cell_left_click_release_event(identifier)
        # We render the view of all cells in case some cell states have been changed to a reveal state.
        for cell_view in self.board_view.cells:
            self.view.set_view(cell_view.identifier, self.board_model)
