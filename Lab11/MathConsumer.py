"""
Creating a PyQt Application:

1- Create a UI file using the QtDesigner.

2- Convert the UI file to a Python file using the conversion tool:
    /package/eda/anaconda3/bin/pyuic5 <fileName.ui> -o <fileName.py>
   The generated file must NOT be modified, as indicated in the header warning!
   
3- Use the given file <MathConsumer.py> to create a consumer Python file, and write the code that drives the UI.

"""

# Import PyQt5 classes
import re
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog

from calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
         super(MathConsumer, self).__init__(parent)
         self.setupUi(self)
         self.btnCalculate.clicked.connect(self.calculate)
         #self.btnCalculate.clicked.connect(performOperation())

         #self.lblNumber1 =
    def calculate(self):
            number1 = 'E'
            number2 = 'E'
            #print(float(self.edtNumber1.text()))
            self.edtNumber1.text()
            pattern ='(?P<number>[+-]?[0-9]*[.][0-9]+)'
            match=re.search(pattern,self.edtNumber1.text())
            if match !=None and match["number"] == self.edtNumber1.text():
                number1 = float(match["number"])
            pattern1 ='(?P<number>[+-]?[0-9]+)'
            match1=re.search(pattern1,self.edtNumber1.text())
            if match == None and match1 != None and match1["number"] == self.edtNumber1.text():
                number1 = int(match1["number"])

            pattern ='(?P<number>[+-]?[0-9]*[.][0-9]+)'
            match=re.search(pattern,self.edtNumber2.text())
            if match !=None and match["number"] == self.edtNumber2.text():
                number2 = float(match["number"])
            pattern1 ='(?P<number>[+-]?[0-9]+)'
            match1=re.search(pattern1,self.edtNumber2.text())
            if match == None and match1 != None and match1["number"] == self.edtNumber2.text():
                number2 = int(match1["number"])

            if number1 == 'E' or number2 == 'E':
                self.edtResult.setText("E")
            else:
                if self.cboOperation.currentText() == "+":
                    self.edtResult.setText(str(number1 + number2))
                elif self.cboOperation.currentText() == "*":
                    self.edtResult.setText(str(number1 * number2))
                elif self.cboOperation.currentText() == "-":
                    self.edtResult.setText(str(number1 - number2))
                elif self.cboOperation.currentText() == "/":
                    if number2 != 0 or number2 != 0.0:
                        self.edtResult.setText(str(number1 / number2))
                    else:
                        self.edtResult.setText("E")

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()
    currentForm.show()
    currentApp.exec_()

