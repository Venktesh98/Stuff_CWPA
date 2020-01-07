from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QMainWindow,QPushButton,QMessageBox,QLabel
import sys

class Windows(QtWidgets.QMainWindow):

    def __init__(self):
        super(Windows,self).__init__()
        self.title = "Dialog box"
        self.open_dialog_box()
    
    def open_dialog_box(self):

        fi = QFileDialog

        '''filename = fi.getOpenFileName()
        path = filename[0]
        print("path is:",path)'''
            
        path = fi.getExistingDirectory(parent=self,caption='Select directory',)
        print("Existing Directory:",path)
        QMessageBox.question(self,"","Directory:"+path,QMessageBox.Ok,QMessageBox.Ok)

app = QtWidgets.QApplication([])
win = Windows()
win.show()
sys.exit(app.exec())
