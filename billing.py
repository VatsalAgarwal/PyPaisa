import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
 
qtCreatorFile = "billing.ui"  # UI File

# I think this needs to be said: DO NOT MAKE THE MISTAKE OF HARDCODING UIs UNLESS IT'S CUSTOM. I blew a 
# long month trying to assemble everything by hand(which I could), before I realised what precious time
# I was wasting in the process. Use Designer(or Qt Creator for C/C++), and spare time for actual backend work.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Calculate.clicked.connect(self.CalcTotal) # Function for Calculate button        	

    def CalcTotal(self):
        Cost1 = self.CostBox.text()
        Cost = int(Cost1)
        Name = str(self.NameBox.text())
        Quantity = int(self.comboBox.currentText())
        Price = str(Cost*Quantity)
        self.TotalLabel.setText(Name+" = "+Price)

        # Self explanatory, but still: The above function computes the 
        # total bill amount from the product of cost and quantity per item.
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
