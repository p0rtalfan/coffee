import sys
from PyQt5.QtWidgets import QApplication,\
    QMainWindow,\
    QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic, \
    QtCore, \
    QtMultimedia
import sqlite3


# main menu form
class MainWidget(QMainWindow):
    # initialization
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/main.ui', self)
        uic.loadUi('UI/addEditCoffeeForm.ui.ui', self)
        self.setWindowTitle('Menu')
        self.pushButton.connect(self.a())
        self.show()


    def a(self):
        con = sqlite3.connect('data/coffee.db')
        cur = con.cursor()
        self.table = cur.execute("SELECT * from coffee").fetchall()
        length = len(self.table)
        for i in range(length):
            self.table[i] = [str(self.table[i][0]).upper(),
                             self.table[i][1],
                             float(self.table[i][2].split(', ')[-1])]
        con.close()
        self.current_table = [] + self.table
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(self.table[0])
        self.show_table(self.current_table)
        self.show()

app = QApplication(sys.argv)
ex = MainWidget()
sys.exit(app.exec_())