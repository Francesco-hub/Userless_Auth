# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        entries = database_read(readable_hash, imageId)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_grades = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_grades.setGeometry(QtCore.QRect(0, 40, 271, 531))
        self.listWidget_grades.setObjectName("listWidget_grades")
        self.listWidget_grades.addItems(entries)
        self.add_grade = QtWidgets.QPushButton(self.centralwidget)
        self.add_grade.setGeometry(QtCore.QRect(290, 470, 141, 31))
        self.add_grade.setObjectName("add_grade")
        self.add_grade.clicked.connect(lambda: addGrade(self.number_grade.value(), readable_hash, imageId))
        self.text_subject = QtWidgets.QLineEdit(self.centralwidget)
        self.text_subject.setGeometry(QtCore.QRect(290, 420, 291, 21))
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
        self.dateEdit.setGeometry(QtCore.QRect(610, 420, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 360, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radioMinus2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioMinus2.setGeometry(QtCore.QRect(310, 270, 21, 21))
        self.radioMinus2.setText("")
        self.radioMinus2.setObjectName("radioMinus2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 210, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 210, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.radio0 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio0.setGeometry(QtCore.QRect(370, 270, 21, 21))
        self.radio0.setText("")
        self.radio0.setObjectName("radio0")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 210, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.radio2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio2.setGeometry(QtCore.QRect(420, 270, 21, 21))
        self.radio2.setText("")
        self.radio2.setObjectName("radio2")
        self.radio4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio4.setGeometry(QtCore.QRect(470, 270, 21, 21))
        self.radio4.setObjectName("radio4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 210, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.radio7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio7.setGeometry(QtCore.QRect(520, 270, 21, 21))
        self.radio7.setObjectName("radio7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(510, 210, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.radio10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio10.setGeometry(QtCore.QRect(570, 270, 21, 21))
        self.radio10.setObjectName("radio10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 210, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.radio12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio12.setGeometry(QtCore.QRect(630, 270, 21, 21))
        self.radio12.setObjectName("radio12")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 210, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(290, 150, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
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
        self.add_grade.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "SUBJECT"))
        self.label_2.setText(_translate("MainWindow", "DATE"))
        self.label_3.setText(_translate("MainWindow", "ENTRIES"))
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