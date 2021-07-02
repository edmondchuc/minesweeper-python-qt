from minesweeper.cell import Cell


class BoardModel:
    def __init__(self, board_size: int):
        self.board_size = board_size

        self.cells = [Cell() for _ in range(board_size)]

    def cell_hover_enter_event(self, identifier: int):
        self.cells[identifier].set_state_hover_enter()

    def cell_hover_leave_event(self, identifier: int):
        self.cells[identifier].set_state_hover_exit()

    def cell_left_click_down_event(self, identifier: int):
        self.cells[identifier].set_state_left_click_down()

    def cell_left_click_release_event(self, identifier: int):
        self.cells[identifier].set_state_left_click_release()
