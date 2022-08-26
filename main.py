# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ravi Scientific Traders")
        self.setGeometry(700,500,400,200)
        self.setStyleSheet("color:red;")
        label1 = QLabel(self)
        label1.setText("Ravi Scientific Traders")
        label1.setStyleSheet("""color: blue; border-style:solid; border-width:2px; border-radius:4px; padding:10px; font:bold 24px Courier;""")
        label1.move(110,40)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
