import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Example')

        widget = QWidget()
        widget1 = QWidget()
        layout = QVBoxLayout()
        layout1 = QVBoxLayout()
        label = QLabel('Hello PyQt6')
        button1 = QPushButton('Button 1')
        layout.addWidget(button1)
        layout1.addWidget(label)
        widget1.setLayout(layout1)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setCentralWidget(widget1)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
