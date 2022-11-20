from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
from PyQt5.QtGui import QColor, QPen, QBrush, QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 151, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Нарисовать окружность"))


class Example(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Супрематизм')
        self.x = 0
        self.y = 0
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawCircle(painter)
        painter.end()

    def drawCircle(self, painter):
        color_1 = random.randint(1, 255)
        color_2 = random.randint(1, 255)
        color_3 = random.randint(1, 255)
        pen = QPen(QColor(color_1, color_2, color_3))
        brush = QBrush(QColor(color_1, color_2, color_3))
        painter.setPen(pen)
        painter.setBrush(brush)
        rad = random.randint(10, 300)
        self.x = random.randint(10, 1000)
        self.y = random.randint(10, 1000)
        painter.drawEllipse(self.x - rad, self.y - rad, rad * 2, rad * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
