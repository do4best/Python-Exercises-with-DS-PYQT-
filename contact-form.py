from PyQt5.QtWidgets import *

class ContactForm(QWidget):
    def __init__(self):
        super().__init__()
        self.startprogramme()

    def startprogramme(self):
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Contact Form")
        self.setTab()
        self.setStyleSheet("background-color:black; color:white")

    def setTab(self):

        self.set_tab = QTabWidget(self) # tab initialized
        self.prof_tab = QWidget()      # profile widget initilize
        self.background_tab = QWidget()    # background widget initilize
        self.set_tab.addTab(self.prof_tab,"Profile Tab")   #profile widget is added to Tab
        self.set_tab.addTab(self.background_tab,"Background") # background widget is add to Tab
        self.profileTabDetails()
        self.backgroundDetails()

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.set_tab)
        self.setLayout(main_h_box)

    def profileTabDetails(self):

        name_label = QLabel("Name")
        name_entry = QLineEdit()

        address_label = QLabel("Address")
        address_entery = QLineEdit()

        sex_gb = QGroupBox("Sex")
        male_rb = QRadioButton("Male")
        femal_rb = QRadioButton("Female")
        sex_h_box = QHBoxLayout()
        sex_h_box.addWidget(male_rb)
        sex_h_box.addWidget(femal_rb)
        sex_gb.setLayout(sex_h_box)

        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(name_label)
        tab_v_box.addWidget(name_entry)
        tab_v_box.addStretch()
        tab_v_box.addWidget(address_label)
        tab_v_box.addWidget(address_entery)
        tab_v_box.addStretch()
        tab_v_box.addWidget(sex_gb)
        self.prof_tab.setLayout(tab_v_box)

    def backgroundDetails(self):
        self.education_gb = QGroupBox("Highest Level of Education")
        ed_v_box = QVBoxLayout()
        education_list = ["High School Diploma","Associate's Degree","Becholar's Degree","Master's Degree","Doctorate or Higher"]
        for ed in education_list:
            self.education_rb = QRadioButton(ed)
            ed_v_box.addWidget(self.education_rb)
        self.education_gb.setLayout(ed_v_box)

        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(self.education_gb)
        self.background_tab.setLayout(tab_v_box)


app = QApplication([])
window = ContactForm()
window.show()
app.exec_()
