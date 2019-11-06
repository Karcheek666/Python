from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,300,300,300)
        self.setWindowTitle("Hello")
        self.line_edit = QLineEdit()
        self.initUI()

    def initUI(self):
        self.textbox = QLineEdit(self)
        self.textbox.move(22, 30)
        self.textbox.resize(220,40)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Enter your name")
        self.label.move(0,0)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Enter")
        self.b1.clicked.connect(self.clicked)
        self.b1.move(60,75)

    def clicked(self):
        self.label.setText("Thanks")
        self.label.move(60,150)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()    