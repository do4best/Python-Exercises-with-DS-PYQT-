import sys

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication, QWidget, QLabel, QGridLayout, QPushButton


# conver celsius to faranheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = fahrenheit - 32
    return celsius
print(celsius_to_fahrenheit(10))
print(fahrenheit_to_celsius(42))

class MyApp(QWidget):
    def __init__(self,fine):
        super().__init__()
        # QMessageBox.about(self, 'Message', str(fine))

        label = QLabel(self)
        grid = QGridLayout()
        grid.addWidget(label, 0, 0)
        label.setText(str(fine))
        push = QPushButton("PushButton",self)
        push.clicked.connect(lambda:print("you Clicked"))
        grid.addWidget(push, 0, 1)
        self.setLayout(grid)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    result = fahrenheit_to_celsius(42)
    myapp = MyApp(result)
    sys.exit(app.exec())