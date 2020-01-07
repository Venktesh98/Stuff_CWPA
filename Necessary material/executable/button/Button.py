from PyQt5.QtWidgets import QApplication ,QWidget,QPushButton,QLabel    
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys

class App(QWidget):

    def __init__(self):

        super().__init__()
        self.title = "Button Window"
        self.left = 50
        self.top = 100
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        #Labels
        self.label = QLabel("Hello world",self)
        self.label.move(120,120)

        #Buttons
        button = QPushButton("Click me",self)
        button.move(119,140)
        button.clicked.connect(self.onClick) 

        button2 = QPushButton("Button2",self)
        button2.move(119,170)
        button2.clicked.connect(self.onClick2)

        #Shows the Window
        self.show()

    @pyqtSlot()
    def onClick(self):
        print("Button1 Clicked:")
    
    @pyqtSlot()
    def onClick2(self):
        print("Button2 Clicked:")
    
app = QApplication(sys.argv)
ob = App()
app.exec_()