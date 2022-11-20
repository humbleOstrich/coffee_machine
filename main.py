import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cappuccino.ui", self)
        self.initUI()
        self.show_data()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Эспрессо')
        self.connection = sqlite3.connect("espresso.db")
        self.tableWidget.itemChanged.connect(self.update_table)
        self.modified = {}
        self.pushButton.clicked.connect(self.add_item)

    def show_data(self):
        cur = self.connection.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.titles = [description[0] for description in cur.description]
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

    def update_table(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.connection.cursor()
            que = "UPDATE coffee SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            print(que)
            cur.execute(que)
            self.connection.commit()
            self.modified.clear()

    def add_item(self):
        values = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
                  self.lineEdit_4.text(),  self.lineEdit_5.text(), self.lineEdit_6.text(),
                  self.lineEdit_7.text()]
        cur = self.connection.cursor()
        que = "INSERT INTO coffee VALUES ("
        que += ", ".join(
            [f"{el}" if i == 0 or i == 5 or i == 6 else f"'{el}'"
             for i, el in enumerate(values)])
        que += ")"
        print(que)
        cur.execute(que)
        self.connection.commit()
        self.show_data()

    def closeEvent(self, event):
        self.save_results()
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())