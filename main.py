import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("espresso.ui", self)
        self.initUI()
        self.show_data()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Эспрессо')
        self.connection = sqlite3.connect("espresso.db")

    def show_data(self):
        cur = self.connection.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.move(0, 0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["id", "название", "степень обжарки",
                                                    "молотый/в зернах", "описание", "цена", "объем упаковки"])
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
