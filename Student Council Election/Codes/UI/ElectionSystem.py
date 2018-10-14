# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ElectionSystem.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StudentElection(object):
    def setupUi(self, StudentElection):
        StudentElection.setObjectName("StudentElection")
        StudentElection.setFixedSize(1000, 600)
        self.pushButtonNext = QtWidgets.QPushButton(StudentElection)
        self.pushButtonNext.setGeometry(QtCore.QRect(949, 0, 51, 600))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonPrev = QtWidgets.QPushButton(StudentElection)
        self.pushButtonPrev.setGeometry(QtCore.QRect(0, 0, 51, 600))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.label = QtWidgets.QLabel(StudentElection)
        self.label.setGeometry(QtCore.QRect(230, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(StudentElection)
        self.radioButton.setGeometry(QtCore.QRect(70, 80, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(StudentElection)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 220, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(StudentElection)
        self.pushButton.setGeometry(QtCore.QRect(150, 350, 241, 31))
        self.pushButton.setObjectName("pushButton")
        directory = os.path.normpath(os.getcwd() + os.sep + os.pardir)
        directory = directory.replace("\\", "/")
        background = ("QWidget#StudentElection{background-image: url(\"" + directory
                            +"/Resources/ElectionSystem.jpg\"); background-position: center;}")
        StudentElection.setStyleSheet(background + open((os.path.normpath(os.getcwd() + os.sep + os.pardir)) +
                                         "\Resources\Design.qss",'r').read())

        self.retranslateUi(StudentElection)
        QtCore.QMetaObject.connectSlotsByName(StudentElection)
        

    def retranslateUi(self, StudentElection):
        _translate = QtCore.QCoreApplication.translate
        StudentElection.setWindowTitle(_translate("StudentElection", "Mapua University"))
        self.pushButtonNext.setText(_translate("StudentElection", "Next"))
        self.pushButtonPrev.setText(_translate("StudentElection", "Prev"))
        self.label.setText(_translate("StudentElection", "Position"))
        self.radioButton.setText(_translate("StudentElection", "Name: "))
        self.radioButton_2.setText(_translate("StudentElection", "Name:"))
        self.pushButton.setText(_translate("StudentElection", "Submit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentElection = QtWidgets.QWidget()
    ui = Ui_StudentElection()
    ui.setupUi(StudentElection)
    StudentElection.show()
    sys.exit(app.exec_())