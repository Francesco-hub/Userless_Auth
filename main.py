import sys
from encodings.base64_codec import base64_encode, base64_decode

import easygui
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import PIL
import mysql.connector
import hashlib
from datetime import datetime
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import pyaes, pbkdf2, binascii, secrets
import base64
import glob
from PIL import Image

currentSalt = None

def getKey(password, salt):
    passwordSalt = salt;
    key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    print('AES encryption key:', binascii.hexlify(key))
    return key


def encrypt(key, data):
    iv = 7
    data = str(data)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(data)
    print(ciphertext)
    ciphertext = binascii.hexlify(ciphertext)
    ciphertext = ciphertext.decode('utf8')
    print('Encrypted: ', ciphertext)
    return ciphertext

    #print('Encrypted and formatted:', binascii.hexlify(ciphertext))

def decrypt (key, encText):
    encText = binascii.unhexlify(encText)
    iv = 7
    print (str(encText))
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(encText)
    return decrypted.decode('utf8')

def database_read(readable_hash, imageId):
    entries = []
    decrypted_entries = []
    currentSalt = None
    imageIdHash = hashlib.sha256(imageId.encode('utf-8')).hexdigest()
    print (imageIdHash)
    string_to_execute = "select user_grade, salt from test_db_1.grades_test where user_id = %s"
    myCursor.execute(string_to_execute, (imageIdHash,))
    try:
        result = myCursor.fetchall()
        for i in result:
            print(i)
            entries.append((i[0]))
            currentSalt = i[1]
        if(currentSalt == None):
            return decrypted_entries, None
        else:
            key = getKey(readable_hash, currentSalt)
        print (entries[0])

        for i in range(0, len(entries)):
            print (i)
            temporal_dec_entry = decrypt(key, str(entries[i]))
            decrypted_entries.append(temporal_dec_entry)

    except:
        decrypted_entries = []

    return decrypted_entries, currentSalt

def confidence(img,template):
  return  (cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED).max())


def addGrade(readable_hash, user_id, uiWindow, currentSalt):
    if(currentSalt == None):
        currentSalt = os.urandom(16)
        currentSalt = binascii.hexlify(currentSalt)
        currentSalt = currentSalt.decode('utf8')
        uiWindow.existingSalt = currentSalt
    imageIdHash = hashlib.sha256(user_id.encode('utf-8')).hexdigest()
    key = getKey(readable_hash, currentSalt)
    print(readable_hash)

    selected_subject = uiWindow.checkSelectedSubject()
    print(selected_subject)
    selected_date = uiWindow.checkDate()
    print(selected_date)
    selected_grade = uiWindow.checkSelectedGrade()
    print("User Id = " + user_id)
    dataString = str(selected_subject) +" | " + str(selected_grade) + " | " + str(selected_date)
    encGrade = encrypt(key,dataString)
    print (str(encGrade))
    string_to_execute = "insert into grades_test(user_id, user_grade, salt) values (%s, %s, %s)"
    val = (str(imageIdHash), str(encGrade), str(currentSalt))
    myCursor.execute(string_to_execute, val)
    myDb.commit()
    print("Db inserted")
    entries = database_read(readable_hash, imageId)[0]
    uiWindow.listWidget_grades.clear()
    uiWindow.listWidget_grades.addItems(entries)



class Ui_MainWindow(object):
    entries = None
    existingSalt = None
    def initData(self, readable_hash, imageId):
        dbRead = database_read(readable_hash, imageId)
        self.entries = dbRead[0]
        self.existingSalt = dbRead[1]
    def setupUi(self, MainWindow, readable_hash, imageId):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_grades = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_grades.setGeometry(QtCore.QRect(0, 40, 271, 531))
        self.listWidget_grades.setObjectName("listWidget_grades")
        self.listWidget_grades.addItems(self.entries)
        self.add_grade = QtWidgets.QPushButton(self.centralwidget)
        self.add_grade.setGeometry(QtCore.QRect(290, 470, 141, 31))
        self.add_grade.setObjectName("add_grade")
        self.add_grade.clicked.connect(lambda: addGrade(readable_hash, imageId, self, self.existingSalt))
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

    def checkSelectedGrade(self):
        if self.radioMinus2.isChecked(): return -2
        if self.radio0.isChecked(): return 0
        if self.radio2.isChecked(): return 2
        if self.radio4.isChecked(): return 4
        if self.radio7.isChecked(): return 7
        if self.radio10.isChecked(): return 10
        if self.radio12.isChecked(): return 12
        else: return None
    def checkSelectedSubject(self):
        return self.text_subject.text()

    def checkDate(self):
        return self.dateEdit.text()


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
def window(readable_hash, imageId):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.initData(readable_hash, imageId)
    ui.setupUi(MainWindow, readable_hash, imageId)
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
    readable_hash = None
    filename = None
    image = None
    imageId = None
    kp1, kp2, mp = None, None, None
    h, w, _ = sample.shape
    myDb = mysql.connector.connect(host="localhost", user="root", passwd="1234567898", database="test_db_1")
    print("Succesfully connected to DB")
    print("-----------------------------")
    myCursor = myDb.cursor()



    counter = 0
    for file in [file for file in os.listdir("assets/registered")]:
        if counter % 10 == 0:
            print(counter)
        counter += 1
        fingerprint_image = cv2.imread("assets/registered/"+ file)
        temp_confidence = confidence(fingerprint_image,sample)
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

    #print ("BEST CONFIDENCE: " + str(best_confidence))
    #print ("SECOND BEST CONFIDENCE: " + str(second_best_confidence))
    #print ("THIRD BEST CONFIDENCE: " + str(third_best_confidence))
    #print ("BEST CONFIDENCE FILE: " +str(best_confidence_file))
    #print ("SECOND BEST CONFIDENCE FILE: " +str(second_best_confidence_file))
    #print ("THIRD BEST CONFIDENCE FILE: " +str(third_best_confidence_file))
    print("BEST MATCH: " + str(filename))
    #print("SCORE: " + str(best_score))
    cv2.waitKey(0)

    if(filename==None):
        save_name = str(int(datetime.timestamp(datetime.now())))
        cv2.imwrite(os.path.join("assets/registered", save_name + ".BMP"), sample)
        matching_file_path = "assets/registered/"+ save_name +".BMP"
        print("saving new image due to no coincidence")
    else:
        matching_file_path = "assets/registered/" + str(filename)
        print("Using existing image coincidence")

    with open(matching_file_path, "rb") as image:
            b= image.read()
            imagename = image.name.replace('assets/registered/', '')
            imageId = imagename.replace('.BMP', '')
            bytes = bytearray(b)  # read entire file as bytes
            readable_hash = hashlib.sha256(bytes).hexdigest();
        #(cv2.imwrite(os.path.join(path, 'doll.jpg'), image))
    '''result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
    result = cv2.resize(result, None, fx=4, fy=4)
    cv2.imshow("Result",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    window(readable_hash, imageId)


