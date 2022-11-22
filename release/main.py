import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QWidget

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 456)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 551, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class Ui_Form_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(920, 509)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 331, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(490, 90, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 120, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(490, 150, 191, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(490, 180, 191, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(490, 210, 191, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(490, 240, 191, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(490, 270, 191, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 321, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(440, 20, 321, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(390, 90, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(390, 130, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(390, 160, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(390, 190, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(390, 220, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(390, 240, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(390, 270, 91, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(390, 330, 251, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Изменение"))
        self.label_2.setText(_translate("Form", "Добавление"))
        self.label_3.setText(_translate("Form", "id"))
        self.label_4.setText(_translate("Form", "название"))
        self.label_5.setText(_translate("Form", "степень обжарки"))
        self.label_6.setText(_translate("Form", "молотый/в зернах"))
        self.label_7.setText(_translate("Form", "описание"))
        self.label_8.setText(_translate("Form", "цена"))
        self.label_9.setText(_translate("Form", "объем"))
        self.pushButton.setText(_translate("Form", "Добавить"))


class Window(QWidget, Ui_Form):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.initUi(args[1])

    def initUi(self, args):
        self.setWindowTitle('Эспрессо')
        self.show_data(args)

    def show_data(self, args):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["id", "название", "степень обжарки",
                                                    "молотый/в зернах", "описание", "цена", "объем упаковки"])
        for i, row in enumerate(args):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


class MainWindow(QMainWindow, Ui_Form_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.show_data()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Капучино')
        self.connection = sqlite3.connect("espresso.db")
        self.tableWidget.itemChanged.connect(self.update_table)
        self.modified = {}
        self.pushButton.clicked.connect(self.add_item)

    def show_data(self):
        cur = self.connection.cursor()
        data = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.new_window = Window(self, data)
        self.new_window.show()
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
            self.show_data()

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
