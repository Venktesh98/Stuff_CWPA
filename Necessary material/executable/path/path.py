import os
from PyQt5.QtWidgets import QApplication ,QWidget,QPushButton,QLabel,QMessageBox,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
from pathlib import Path

class App(QWidget):

    def __init__(self):

        super().__init__()
        self.title = "Button Window"
        self.left = 50
        self.top = 100
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        #Labels
        self.label = QLabel("Hello world",self)
        self.label.move(120,120)
        self.label.resize(350,250)

        #Buttons
        button = QPushButton("Click me",self)
        button.move(119,140)
        button.clicked.connect(self.onClick) 

        # self.textbox = QLineEdit(self)
        # self.textbox.move(120,180)
        # self.textbox.resize(400,20)
        #self.button.
        # button2 = QPushButton("Button2",self)
        # button2.move(119,170)
        # button2.clicked.connect(self.onClick2)

        #Shows the Window
        self.show()

    @pyqtSlot()
    def onClick(self):
        print("Button1 Clicked:")
        
        #gets current directory
        currentDirectory = os.getcwd()
        print("current Directory path:",currentDirectory)
        QMessageBox.question(self,"","Directory:"+currentDirectory,QMessageBox.Ok,QMessageBox.Ok)

        currentfile = Path(__file__).absolute()
        print("current File path:",currentfile)
        self.label.setText(str(currentfile))
        #self.textbox.setText(currentfile)
        

        #Another method
        #print("Directory path:",Path().absolute())

        #print("File      Path:", Path(__file__).absolute()
    
    # @pyqtSlot()
    # def onClick2(self):
    #     print("Button2 Clicked:")
    #     currentfile = Path(__file__).absolute()
    #     print("current File path:",currentfile)
    #     QMessageBox.question(self,"","File:",str(currentfile))

        
    
app = QApplication(sys.argv)
ob = App()
app.exec_()


 
# def main():
    
#     '''
#         Get Current working Directory
#     '''
#     currentDirectory = os.getcwd()
    
#     print(currentDirectory)
    
#     '''
#         Change the Current working Directory
#     '''
#     # os.chdir('/home/varun')
    
#     # '''
#     #     Get Current working Directory
#     # '''
#     # currentDirectory = os.getcwd()
    
#     # print(currentDirectory)
        
# if __name__ == '__main__':
#     main()
