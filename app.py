from PySide6.QtWidgets import QApplication

from minesweeper import MainWindow

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
