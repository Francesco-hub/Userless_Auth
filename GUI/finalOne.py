# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalOne.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_grade = QtWidgets.QPushButton(self.centralwidget)
        self.add_grade.setGeometry(QtCore.QRect(660, 460, 141, 31))
        self.add_grade.setObjectName("add_grade")
        self.text_subject = QtWidgets.QLineEdit(self.centralwidget)
        self.text_subject.setGeometry(QtCore.QRect(660, 410, 291, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_subject.sizePolicy().hasHeightForWidth())
        self.text_subject.setSizePolicy(sizePolicy)
        self.text_subject.setMaximumSize(QtCore.QSize(370, 16777215))
        self.text_subject.setSizeIncrement(QtCore.QSize(0, 7))
        self.text_subject.setText("")
        self.text_subject.setObjectName("text_subject")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(980, 410, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 350, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(980, 350, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radioMinus2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioMinus2.setGeometry(QtCore.QRect(710, 250, 21, 21))
        self.radioMinus2.setText("")
        self.radioMinus2.setObjectName("radioMinus2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(690, 190, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(760, 190, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.radio0 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio0.setGeometry(QtCore.QRect(770, 250, 21, 21))
        self.radio0.setText("")
        self.radio0.setObjectName("radio0")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(810, 190, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.radio2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio2.setGeometry(QtCore.QRect(820, 250, 21, 21))
        self.radio2.setText("")
        self.radio2.setObjectName("radio2")
        self.radio4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio4.setGeometry(QtCore.QRect(870, 250, 21, 21))
        self.radio4.setObjectName("radio4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(860, 190, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.radio7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio7.setGeometry(QtCore.QRect(920, 250, 21, 21))
        self.radio7.setObjectName("radio7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(910, 190, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.radio10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio10.setGeometry(QtCore.QRect(970, 250, 21, 21))
        self.radio10.setObjectName("radio10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(960, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.radio12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio12.setGeometry(QtCore.QRect(1030, 250, 21, 21))
        self.radio12.setObjectName("radio12")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1020, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(660, 150, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.listWidget_Subject = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Subject.setGeometry(QtCore.QRect(0, 60, 201, 481))
        self.listWidget_Subject.setObjectName("listWidget_Subject")
        self.listWidget_Date = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Date.setGeometry(QtCore.QRect(200, 60, 201, 481))
        self.listWidget_Date.setObjectName("listWidget_Date")
        self.listWidget_Grade = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Grade.setGeometry(QtCore.QRect(400, 60, 201, 481))
        self.listWidget_Grade.setObjectName("listWidget_Grade")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(260, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
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
        self.add_grade.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "SUBJECT"))
        self.label_2.setText(_translate("MainWindow", "DATE"))
        self.label_3.setText(_translate("MainWindow", "SUBJECT"))
        self.label_4.setText(_translate("MainWindow", "-2"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "2"))
        self.radio4.setText(_translate("MainWindow", "4"))
        self.label_7.setText(_translate("MainWindow", "4"))
        self.radio7.setText(_translate("MainWindow", "7"))
        self.label_8.setText(_translate("MainWindow", "7"))
        self.radio10.setText(_translate("MainWindow", "10"))
        self.label_9.setText(_translate("MainWindow", "10"))
        self.radio12.setText(_translate("MainWindow", "12"))
        self.label_10.setText(_translate("MainWindow", "12"))
        self.label_11.setText(_translate("MainWindow", "GRADE"))
        self.label_12.setText(_translate("MainWindow", "DATE"))
        self.label_13.setText(_translate("MainWindow", "GRADE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())