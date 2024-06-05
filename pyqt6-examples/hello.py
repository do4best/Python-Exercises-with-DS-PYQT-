import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout
from PyQt6.QtGui import QPalette, QColor



class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        different = ['red', 'blue', 'green', 'yellow', 'black', 'white']
        for _ in different:
            layout.addWidget(Color(_))


        self.setWindowTitle("My App")
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()