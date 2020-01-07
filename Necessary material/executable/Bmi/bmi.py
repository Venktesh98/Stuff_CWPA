# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(210, 170, 121, 121))
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 10, 271, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setObjectName("gridLayout2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout2.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout2.addWidget(self.label_2, 3, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn1.setObjectName("btn1")
        self.gridLayout2.addWidget(self.btn1, 7, 0, 1, 1)
        self.lineEdit1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.gridLayout2.addWidget(self.lineEdit1, 2, 0, 1, 1)
        self.lineEdit2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.gridLayout2.addWidget(self.lineEdit2, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout2.addWidget(self.label_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Length"))
        self.label_2.setText(_translate("MainWindow", "Weight"))
        self.btn1.setText(_translate("MainWindow", "Calculate"))
        self.label_4.setText(_translate("MainWindow", "BMI Calculater"))

        self.btn1.clicked.connect(self.onClick)

    def onClick(self):
        print("Button Clicked:")
        height = float(self.lineEdit1.text())
        mass = float(self.lineEdit2.text())
        bmi = mass/(height * height)
        bmi = round(bmi,3)
        self.label3.setText("BMI is:"+str(bmi))
        print("Bmi:"+str(bmi))
       



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

