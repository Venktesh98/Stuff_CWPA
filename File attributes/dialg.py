from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QMainWindow,QPushButton
import shutil,os
import sys



# def btn1(self) :
#     print("Copy Button is pressed.")
#     uic.loadUi("dialog.ui",self)
#     self.open_dialog_box()

class Windows(QtWidgets.QMainWindow):

    def __init__(self):
        super(Windows,self).__init__()
        self.title = "Dialog box"
        uic.loadUi("/home/venktesh/Desktop/dailog.ui",self)
        #self.open_dialog_box()
        self.btn1.clicked.connect(self.open_dialog_box)

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print("path is:",path)

        fi = QFileInfo(path)
        filename_only = fi.fileName()
        print("FileName:",filename_only)

        file_size = fi.size()
        print("File Size:",file_size,"bytes")

        file_basename = fi.baseName()
        print("Basename:",file_basename)

        file_extension = fi.suffix()
        print("File Extension:.",file_extension)

        # filenameonly = QFileInfo(path).fileName()
        # print("Only name of File is:",filenameonly)
        # filesize = QFileInfo(path).size()
        # print("Only filesize is:",filesize)
        # basename = QFileInfo(path).baseName()
        # print("Only Basename is",basename)
        # file_extension = QFileInfo(path).suffix()
        # print("Only file extension:",file_extension)
        self.show()
        #shutil.copy(path,'/home/venktesh/Desktop/Copy')

app = QtWidgets.QApplication([])
win = Windows()
win.show()
sys.exit(app.exec())
