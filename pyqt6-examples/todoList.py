import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, \
    QGridLayout, QCheckBox,QTextEdit
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

        close_button = QPushButton("close")
        close_button.clicked.connect(self.close)

        #create section Label
        mustdo_label = QLabel("Must Do")
        mustdo_label.setFont(QFont("Arial", 24))
        mustdo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        appts_label = QLabel("Appointments")
        appts_label.setFont(QFont("Arial", 20))
        appts_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5,5,5,5)
        mustdo_grid.addWidget(mustdo_label,0,0,1,2)
        #create checkbox and line edit widget
        for position in range(1,15):
            checkBox = QCheckBox()
            checkBox.setChecked(False)
            lineEdit = QLineEdit()
            lineEdit.setMinimumWidth(200)
            mustdo_grid.addWidget(checkBox,position,0)
            mustdo_grid.addWidget(lineEdit,position,1)
        #create label for appointemnt position
        mourning_label = QLabel("Mourning")
        mourning_label.setFont(QFont("Arial", 16))
        mourning_entry = QTextEdit()
        noon_label = QLabel("Noon")
        noon_label.setFont(QFont("Arial", 16))
        noon_entry = QTextEdit()
        evening_label = QLabel("Evening")
        evening_label.setFont(QFont("Arial", 16))
        evening_entry = QTextEdit()
        #create vertical layout
        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5,5,5,5)
        appt_v_box.addWidget(appts_label)
        appt_v_box.addWidget(mourning_label)
        appt_v_box.addWidget(mourning_entry)
        appt_v_box.addWidget(noon_label)
        appt_v_box.addWidget(noon_entry)
        appt_v_box.addWidget(evening_label)
        appt_v_box.addWidget(evening_entry)
        main_grid.addWidget(todo_list,0,0,1,2)
        main_grid.addLayout(mustdo_grid,1,0)
        main_grid.addLayout(appt_v_box,1,1)
        main_grid.addLayout(mustdo_grid,2,0,1,2)
        self.setLayout(main_grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = TodoList()
    app.exec()