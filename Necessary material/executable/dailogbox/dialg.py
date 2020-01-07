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
        #uic.loadUi("/home/venktesh/Desktop/dailog.ui",self)
        self.open_dialog_box()
        #self.btn1.clicked.connect(self.open_dialog_box)
        # QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        # self.setToolTip("System Tray:")

    # def __init__(self, icon, parent=None):
        # QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        # self.setToolTip("System Tray:")

    def open_dialog_box(self):

        fi = QFileDialog

        '''filename = fi.getOpenFileName()
        path = filename[0]
        print("path is:",path)'''
            
        path = fi.getExistingDirectory(parent=self,caption='Select directory',)
        print("Existing Directory:",path)
        QMessageBox.question(self,"","Directory:"+path,QMessageBox.Ok,QMessageBox.Ok)
        sys.exit(fi.exec(self))


        

        #self.show()

    ''' 
        fi = QFileInfo(path)
        filename_only = fi.fileName()
        print("FileName:",filename_only)

        file_size = fi.size()
        print("File Size:",file_size,"bytes")

        file_basename = fi.baseName()
        print("Basename:",file_basename)

        file_extension = fi.suffix()
        print("File Extension:.",file_extension)
    '''

        # filenameonly = QFileInfo(path).fileName()
        # print("Only name of File is:",filenameonly)
        # filesize = QFileInfo(path).size()
        # print("Only filesize is:",filesize)
        # basename = QFileInfo(path).baseName()
        # print("Only Basename is",basename)
        # file_extension = QFileInfo(path).suffix()
        # print("Only file extension:",file_extension)
        # self.show()
        #shutil.copy(path,'/home/venktesh/Desktop/Copy')

app = QtWidgets.QApplication([])
win = Windows()
win.show()
sys.exit(app.exec())

# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     w = QtWidgets.QWidget()
#     tray_icon = Windows(QtGui.QIcon("systray.jpeg"), w)
#     tray_icon.show()
#     tray_icon.showMessage('System Tray', ' "Welcome:" ')
#     sys.exit(app.exec_())

# main()

