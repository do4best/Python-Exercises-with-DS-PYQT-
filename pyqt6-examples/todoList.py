import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QGridLayout
from PyQt6.QtCore import Qt


class TodoList(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,500,500)
        self.setWindowTitle('The Todo List')
        self.setUp()
        self.show()

    def setUp(self):
        main_grid = QGridLayout()
        todo_list = QLabel("Todo List",alignment=Qt.AlignmentFlag.AlignCenter)
        todo_list.setFont(QFont("Arial", 24))







if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = TodoList()
    app.exec()