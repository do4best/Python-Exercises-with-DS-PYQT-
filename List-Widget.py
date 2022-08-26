from PyQt5.QtWidgets import *
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.startProgramme()

    def startProgramme(self):

        self.setWindowTitle("Ravi Scientific Traders")
        self.setGeometry(700,500,400,200)
        self.setupWidget()

    def setupWidget(self):
        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)
        grocery_list = ["grapes","broccoli","garlic","cheese","bacon","eggs","waffle","rice","soda"]
        for item in grocery_list:
            list_item = QListWidgetItem()
            list_item.setText(item)
            self.list_widget.addItem(list_item)

        #cretes buttons
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.addListItem)

        insert_button = QPushButton("Insert")
        insert_button.clicked.connect(self.insertItemInList)

        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.removeOneItem)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.list_widget.clear)

        #Creating Layour
        right_v_box = QVBoxLayout()
        right_v_box.addWidget(add_button)
        right_v_box.addWidget(insert_button)
        right_v_box.addWidget(remove_button)
        right_v_box.addWidget(clear_button)

        left_h_box = QHBoxLayout()
        left_h_box.addWidget(self.list_widget)
        left_h_box.addLayout(right_v_box)
        self.setLayout(left_h_box)

    def addListItem(self):
        # Add a single item to the list
        text,ok = QInputDialog.getText(self,"New Item","Add Item:")
        if ok and text != "":
            list_item = QListWidgetItem()
            list_item.setText(text)
            self.list_widget.addItem(list_item)

    def insertItemInList(self):

        text,ok = QInputDialog.getText(self,"Insert Item","Insert Item: ")
        if ok and text != "":
            row = self.list_widget.currentRow()
            row = row + 1
            new_item = QListWidgetItem()
            new_item.setText(text)
            self.list_widget.insertItem(row,new_item)

    def removeOneItem(self):
        row = self.list_widget.currentRow()
        self.list_widget.takeItem(row)

        self.setStyleSheet("color:red;")
        label1 = QLabel(self)
        label1.setText("Ravi Scientific Traders")
        label1.setStyleSheet("""color: blue; border-style:solid; border-width:2px; border-radius:4px; padding:10px; font:bold 24px Courier;""")
        label1.move(110,40)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
