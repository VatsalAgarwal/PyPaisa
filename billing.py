# I'm sorry, but until I figure this out, you'll have to have a MySQL Test databse 
# up and running for the script to work. I've added some defaults, but feel free to 
# substitute your own. I profusely apologise for the inconvenience.

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
        
     def SaveSQL(self):
        db = MySQLdb.connect('localhost','name','password','PyPaisaDB')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS 'PYPAISADB'.'PYPAISA'('Cost' float(4,5) not null, 'Name' varchar(20) not null, 'Quantity' int not null, Price long not null;")
        sql= """INSERT INTO PYPAISA(COST, NAME, QUANTITY, PRICE) VALUES({},{},{},{})""".format(Cost, Name, Quantity, Price)

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        
        db.close()

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
