from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QMainWindow,QPushButton,QMessageBox,QLabel
import shutil,os
import sys
from pathlib import Path


# def btn1(self) :
#     print("Copy Button is pressed.")
#     uic.loadUi("dialog.ui",self)
#     self.open_dialog_box()

class Windows(QtWidgets.QMainWindow):

    def __init__(self):
        super(Windows,self).__init__()
        self.title = "Dialog box"
        self.open_dialog_box()

    def open_dialog_box(self):

        fi = QFileDialog
        # self.label = QLabel()
        # self.label.resize(2002,300)

        '''filename = fi.getOpenFileName()
        path = filename[0]
        print("path is:",path)'''
            
        path = fi.getExistingDirectory(parent=self,caption='Select directory',)
        # fopen = open("uuid.txt","r")
        print("Existing Directory:",path)
        QMessageBox.information(self,"","Directory:"+path+"/uuid.txt",QMessageBox.Ok,QMessageBox.Ok)
        # self.label.setText(path+"/uuid.txt")
        #sys.exit(fi.exec(self))
        #fi.exec_(self)
        self.show()
        # fopen.close
        

app = QtWidgets.QApplication([])
win = Windows()
win.show()
sys.exit(app.exec())

