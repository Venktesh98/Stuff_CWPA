from PyQt5 import QtWidgets,uic
import sys
from bmi import Ui_MainWindow

class Bmi:
    def Qt_call(self):
 #   if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    # def onClick(self):
    #     print("Button Clicked:")
    #     height = float(self.lineEdit1.text())
    #     mass = float(self.lineEdit2.text())
    #     bmi = mass/(height * height)
    #     bmi = round(bmi,3)
    #     self.label3.setText("BMI is:"+str(bmi))
    #     print("Bmi:"+str(bmi))
       


# app = QtWidgets.QApplication([])
win = Bmi()
win.Qt_call()
# sys.exit(app.exec())