from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.startProgramme()

    def startProgramme(self):

        self.setGeometry(100,100,350,350)
        self.setWindowTitle("Basic Meny")
        self.setCentralWidget(QTextEdit())

        self.createMenu()
        self.createToolBar()
        self.createDockWiget()

    def createMenu(self):

        self.exit_act = QAction(QIcon('exit-icon.png'),'Exit',self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setToolTip('Quit programme')
        self.exit_act.triggered.connect(self.close)
        #create action for view menu
        full_screen_act = QAction('Full Screen',self,checkable=True)
        full_screen_act.setStatusTip('Switch to full screen Mood')
        full_screen_act.triggered.connect(self.switchToFullScreen)
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        file_menu = menubar.addMenu('File')
        file_menu.addAction(self.exit_act)

        view_menu = menubar.addMenu('View')
        apperance_submenu = view_menu.addMenu('Appearance')
        apperance_submenu.addAction(full_screen_act)
        self.setStatusBar(QStatusBar(self))

    def createToolBar(self):
        tool_bar = QToolBar("Main Toolbar")
        tool_bar.setIconSize(QSize(16,16))
        self.addToolBar(tool_bar)
        tool_bar.addAction(self.exit_act)

    def createDockWiget(self):

        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Example Dock")
        dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)

        dock_widget.setWidget(QTextEdit())

        self.addDockWidget(Qt.LeftDockWidgetArea,dock_widget)

    def switchToFullScreen(self,state):

        if state:
            self.showFullScreen()
        else:
            self.showNormal()


if __name__ == "__main__":
    app = QApplication([])
    window = MainMenu()
    window.show()
    app.exec_()
