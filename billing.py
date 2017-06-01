import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
 
qtCreatorFile = "billing.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Calculate.clicked.connect(self.CalcTotal)
        	

    def CalcTotal(self):
        Cost1 = self.CostBox.text()
        Cost = int(Cost1)
        Name = str(self.NameBox.text())
        Quantity = int(self.comboBox.currentText())
        Price = str(Cost*Quantity)
        self.TotalLabel.setText(Name+" = "+Price)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
