

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 589)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Hello = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_Hello.setGeometry(QtCore.QRect(290, 150, 171, 31))
        self.label_Hello.setObjectName("label_Hello")
        self.pushButton_create = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(110, 320, 131, 61))
        self.pushButton_create.setObjectName("pushButton_create")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(250, 220, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 250, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 280, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 220, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 250, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 280, 131, 21))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 310, 201, 71))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.addItems(["green", "white", "blue"])
        self.comboBox_2.addItems(["blue", "purple", "orange"])
        self.comboBox_3.addItems(["black", "red", "Brown"])
        self.pushButton_create.clicked.connect(self.draw_button_clicked)

    def draw_button_clicked(self):
        color1 = self.comboBox.currentText()
        color2 = self.comboBox_2.currentText()
        color3 = self.comboBox_3.currentText()
        self.textEdit.clear()


        self.textEdit.setTextColor(QtGui.QColor(color1))
        self.textEdit.append(color1)

        self.textEdit.setTextColor(QtGui.QColor(color2))
        self.textEdit.append(color2)

        self.textEdit.setTextColor(QtGui.QColor(color3))
        self.textEdit.append(color3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Hello.setText(_translate("MainWindow", "Текстовый флаг М.В.А 4ИСПК1"))
        self.pushButton_create.setText(_translate("MainWindow", "Нарисовать"))
        self.label.setText(_translate("MainWindow", "Изменить первый цвет"))
        self.label_2.setText(_translate("MainWindow", "Изменить второй цвет"))
        self.label_3.setText(_translate("MainWindow", "Изменить третий цвет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
