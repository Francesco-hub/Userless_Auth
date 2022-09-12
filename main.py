import sys
import easygui
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow
import PIL
import mysql.connector


def confidence(img,template):
  return  (cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED).max())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(290, 330, 221, 181))
        self.button1.setObjectName("button1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(360, 140, 221, 16))
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "Press Me"))
        self.label1.setText(_translate("MainWindow", "Hello Pepaitus"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
'''class MyWindow(QMainWindow):
    def __init__(self):
        super (MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Hello Pepo")
        self.initUI()
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Pepito")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Button is pressed")
        self.update()

    def update(self):
        self.label.adjustSize()

def clicked():
    print("clicked")'''
def window():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    Tk().withdraw()
    importedFilename = askopenfilename()
    sample = cv2.imread(importedFilename)
    print (importedFilename)
    best_score = 0
    best_confidence = 0
    best_confidence_file = None
    second_best_confidence = 0
    second_best_confidence_file = None
    third_best_confidence = 0
    third_best_confidence_file = None
    filename = None
    image = None
    kp1, kp2, mp = None, None, None
    h, w, _ = sample.shape


    counter = 0
    for file in [file for file in os.listdir("assets/registered")]:
        if counter % 10 == 0:
            print(counter)
        counter += 1
        fingerprint_image = cv2.imread("assets/registered/"+ file)
        temp_confidence = confidence(fingerprint_image,sample)
        print(temp_confidence)
        if(temp_confidence > best_confidence):
            best_confidence = temp_confidence
            best_confidence_file = file
        elif(temp_confidence > second_best_confidence):
            second_best_confidence = temp_confidence
            second_best_confidence_file = file
        elif(temp_confidence > third_best_confidence):
            third_best_confidence =temp_confidence
            third_best_confidence_file = file
        sift = cv2.SIFT_create()


        keypoints_1 , descriptors_1 = sift.detectAndCompute(sample, None)
        keypoints_2 , descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

        matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10},
                                    {}).knnMatch(descriptors_1, descriptors_2, k=2)

        match_points = []

        for p, q in matches:
            if p.distance < 0.1 * q.distance:
                match_points.append(p)

        keypoints = 0
        if len(keypoints_1) < len(keypoints_2):
            keypoints = len(keypoints_1)
        else:
            keypoints = len(keypoints_2)

        if len(match_points)/ keypoints * 100 > best_score:
                best_score = len(match_points) / keypoints * 100
                filename = file
                image = fingerprint_image
                kp1, kp2, mp = keypoints_1, keypoints_2, match_points

    print ("BEST CONFIDENCE: " + str(best_confidence))
    print ("SECOND BEST CONFIDENCE: " + str(second_best_confidence))
    print ("THIRD BEST CONFIDENCE: " + str(third_best_confidence))
    print ("BEST CONFIDENCE FILE: " +str(best_confidence_file))
    print ("SECOND BEST CONFIDENCE FILE: " +str(second_best_confidence_file))
    print ("THIRD BEST CONFIDENCE FILE: " +str(third_best_confidence_file))
    print("BEST MATCH: " + str(filename))
    print("SCORE: " + str(best_score))
    cv2.waitKey(0)

    if(filename==None):
        cv2.imwrite(os.path.join("assets/registered", "Test1.BMP"), sample)
        #(cv2.imwrite(os.path.join(path, 'doll.jpg'), image))
    '''result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
    result = cv2.resize(result, None, fx=4, fy=4)
    cv2.imshow("Result",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    window()


