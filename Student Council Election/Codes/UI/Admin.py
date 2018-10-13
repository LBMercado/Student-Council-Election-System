# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lauren\Desktop\Admin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from BusinessLogic.Election import Election
from BusinessLogic.AdminInterface import AdminInterface
from BusinessLogic.Admin import Admin
from datetime import datetime, timedelta

class Ui_Admin(object):
    def setupUi(self, Admin):
        #   custom variables
        self.election_duration = 10 #   set in program
        self.projDirectory = os.getcwd()
        self.user = None
        self.adminInterface = None

        Admin.setObjectName("Admin")
        Admin.setFixedSize(1000, 600)
        self.pushButtonCreateUser = QtWidgets.QPushButton(Admin)
        self.pushButtonCreateUser.setGeometry(QtCore.QRect(50, 100, 150, 50))
        self.pushButtonCreateUser.setObjectName("pushButtonCreateUser")
        self.pushButtonDeleteUser = QtWidgets.QPushButton(Admin)
        self.pushButtonDeleteUser.setGeometry(QtCore.QRect(50, 170, 150, 50))
        self.pushButtonDeleteUser.setObjectName("pushButtonDeleteUser")
        self.pushButtonEditUser = QtWidgets.QPushButton(Admin)
        self.pushButtonEditUser.setGeometry(QtCore.QRect(50, 240, 150, 50))
        self.pushButtonEditUser.setObjectName("pushButtonEditUser")
        self.pushButtonStartElec = QtWidgets.QPushButton(Admin)
        self.pushButtonStartElec.setGeometry(QtCore.QRect(50, 310, 150, 50))
        self.pushButtonStartElec.setObjectName("pushButtonStartElec")
        self.pushButtonEndElec = QtWidgets.QPushButton(Admin)
        self.pushButtonEndElec.setGeometry(QtCore.QRect(50, 380, 150, 50))
        self.pushButtonEndElec.setObjectName("pushButtonEndElec")
        self.pushButtonSummary = QtWidgets.QPushButton(Admin)
        self.pushButtonSummary.setGeometry(QtCore.QRect(50, 450, 150, 50))
        self.pushButtonSummary.setObjectName("pushButtonSummary")
        self.scrollAreaCreateUser = QtWidgets.QScrollArea(Admin)
        self.scrollAreaCreateUser.setGeometry(QtCore.QRect(240, 100, 721, 401))
        self.scrollAreaCreateUser.setWidgetResizable(True)
        self.scrollAreaCreateUser.setObjectName("scrollAreaCreateUser")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lineEditName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditName.setGeometry(QtCore.QRect(140, 30, 461, 41))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditStudentNum = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditStudentNum.setGeometry(QtCore.QRect(140, 100, 461, 41))
        self.lineEditStudentNum.setObjectName("lineEditStudentNum")
        self.lineEditPass = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPass.setGeometry(QtCore.QRect(140, 170, 461, 41))
        self.lineEditPass.setObjectName("lineEditPass")
        self.lineEditReenterPass = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditReenterPass.setGeometry(QtCore.QRect(140, 240, 461, 41))
        self.lineEditReenterPass.setObjectName("lineEditReenterPass")
        self.pushButtonCreate = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonCreate.setGeometry(QtCore.QRect(280, 320, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonCreate.setFont(font)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.scrollAreaCreateUser.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(Admin)
        self.pushButton.setGeometry(QtCore.QRect(910, 20, 51, 51))
        self.pushButton.setObjectName("pushButton")
        self.scrollAreaDelete = QtWidgets.QScrollArea(Admin)
        self.scrollAreaDelete.setGeometry(QtCore.QRect(240, 100, 721, 401))
        self.scrollAreaDelete.setWidgetResizable(True)
        self.scrollAreaDelete.setObjectName("scrollAreaDelete")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 719, 399))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.lineEditSearch = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEditSearch.setGeometry(QtCore.QRect(60, 40, 461, 41))
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.pushButtonSearch = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButtonSearch.setGeometry(QtCore.QRect(560, 40, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.labelDelProfile = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelDelProfile.setGeometry(QtCore.QRect(60, 120, 581, 171))
        self.labelDelProfile.setWordWrap(True)
        self.labelDelProfile.setObjectName("labelDelProfile")
        self.pushButtonDelete = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButtonDelete.setGeometry(QtCore.QRect(280, 320, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.scrollAreaDelete.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollAreaEdit = QtWidgets.QScrollArea(Admin)
        self.scrollAreaEdit.setGeometry(QtCore.QRect(240, 100, 721, 401))
        self.scrollAreaEdit.setWidgetResizable(True)
        self.scrollAreaEdit.setObjectName("scrollAreaEdit")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 719, 399))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.lineEditSearchEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEditSearchEdit.setGeometry(QtCore.QRect(20, 20, 461, 41))
        self.lineEditSearchEdit.setObjectName("lineEditSearchEdit")
        self.pushButtonSearchEdit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButtonSearchEdit.setGeometry(QtCore.QRect(500, 20, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSearchEdit.setFont(font)
        self.pushButtonSearchEdit.setObjectName("pushButtonSearchEdit")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 281, 151))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButtonEdit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButtonEdit.setGeometry(QtCore.QRect(280, 320, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonEdit.setFont(font)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit.setGeometry(QtCore.QRect(330, 110, 371, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 170, 371, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 230, 371, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.scrollAreaEdit.setWidget(self.scrollAreaWidgetContents_4)
        self.labelElectionStatus = QtWidgets.QLabel(Admin)
        self.labelElectionStatus.setGeometry(QtCore.QRect(60, 520, 451, 71))
        self.labelElectionStatus.setObjectName("labelElectionStatus")
        self.scrollAreaSumm = QtWidgets.QScrollArea(Admin)
        self.scrollAreaSumm.setGeometry(QtCore.QRect(240, 100, 721, 401))
        self.scrollAreaSumm.setWidgetResizable(True)
        self.scrollAreaSumm.setObjectName("scrollAreaSumm")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 719, 399))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBoxPosition = QtWidgets.QComboBox(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPosition.sizePolicy().hasHeightForWidth())
        self.comboBoxPosition.setSizePolicy(sizePolicy)
        self.comboBoxPosition.setMinimumSize(QtCore.QSize(400, 40))
        self.comboBoxPosition.setObjectName("comboBoxPosition")
        self.verticalLayout_3.addWidget(self.comboBoxPosition)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(120, 120))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(120, 120))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.scrollAreaSumm.setWidget(self.scrollAreaWidgetContents_5)

        projDirectory = self.projDirectory.replace("\\", "/")
        background = ("QWidget#Admin{background-image: url(\""+projDirectory
                            +"/Resources/LogInBackground.jpg\"); background-position: center;}")
        Admin.setStyleSheet(background + open(self.projDirectory
                            + "\Resources\Design.qss",'r').read())
        Admin.setWindowIcon(QtGui.QIcon(self.projDirectory
                            + "\Resources\MapuaIcon.png"))      
        font.setPointSize(14)
        self.pushButtonCreateUser.setFont(font)
        self.pushButtonDeleteUser.setFont(font)
        self.pushButtonEditUser.setFont(font)
        self.pushButtonStartElec.setFont(font)
        self.pushButtonEndElec.setFont(font)
        font.setPointSize(10)
        self.pushButtonSummary.setFont(font)
        font.setPointSize(16)
        self.lineEditName.setFont(font)
        self.lineEditStudentNum.setFont(font)
        self.lineEditPass.setFont(font)
        self.lineEditReenterPass.setFont(font)
        self.lineEditSearch.setFont(font)
        self.lineEditSearchEdit.setFont(font)
        self.lineEdit.setFont(font)
        self.lineEdit_2.setFont(font)
        self.lineEdit_3.setFont(font)
        self.lineEditName.setStyleSheet("color: gray")
        self.lineEditStudentNum.setStyleSheet("color: gray")
        self.lineEditPass.setStyleSheet("color: gray")
        self.lineEditReenterPass.setStyleSheet("color: gray")
        self.lineEditSearch.setStyleSheet("color: gray")
        self.lineEditSearchEdit.setStyleSheet("color: gray")
        self.lineEdit.setStyleSheet("color: gray")
        self.lineEdit_2.setStyleSheet("color: gray")
        self.lineEdit_3.setStyleSheet("color: gray")
        self.lineEditName.setPlaceholderText("LastName, GivenName MI")
        self.lineEditStudentNum.setPlaceholderText("Student number")
        self.lineEditPass.setPlaceholderText("Password")
        self.lineEditReenterPass.setPlaceholderText("Reenter password")
        self.lineEditSearch.setPlaceholderText("Student number")
        self.lineEditSearchEdit.setPlaceholderText("Student number")
        self.lineEdit.setPlaceholderText("Name")
        self.lineEdit_2.setPlaceholderText("Student number")
        self.lineEdit_3.setPlaceholderText("Email")
        self.scrollAreaCreateUser.hide()
        self.scrollAreaDelete.hide()
        self.scrollAreaEdit.hide()
        self.scrollAreaSumm.hide()
        self.retranslateUi(Admin)
        font.setPointSize(20)
        self.comboBoxPosition.setFont(font)
        self.comboBoxPosition.addItem("PRESIDENT")
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Mapua University"))
        self.pushButtonCreateUser.setText(_translate("Admin", "Create User"))
        self.pushButtonDeleteUser.setText(_translate("Admin", "Delete User"))
        self.pushButtonEditUser.setText(_translate("Admin", "Edit User"))
        self.pushButtonStartElec.setText(_translate("Admin", "Start Election"))
        self.pushButtonEndElec.setText(_translate("Admin", "End Election"))
        self.pushButtonSummary.setText(_translate("Admin", "See Summary of Votes"))
        self.pushButtonCreate.setText(_translate("Admin", "Create"))
        self.pushButton.setText(_translate("Admin", "Signout"))
        self.pushButtonSearch.setText(_translate("Admin", "Search"))
        self.labelDelProfile.setText(_translate("Admin", "<html><head/><body><p><span style=\" font-size:20pt;\">Name: </span></p><p><span style=\" font-size:20pt;\">Student Number: </span></p><p><span style=\" font-size:20pt;\">Email:</span></p></body></html>"))
        self.pushButtonDelete.setText(_translate("Admin", "Delete"))
        self.pushButtonSearchEdit.setText(_translate("Admin", "Search"))
        self.label_2.setText(_translate("Admin", "<html><head/><body><p><span style=\" font-size:10pt;\">Name: </span></p><p><span style=\" font-size:10pt;\">Student Number: </span></p><p><span style=\" font-size:10pt;\">Email:</span></p></body></html>"))
        self.pushButtonEdit.setText(_translate("Admin", "Edit"))

        #   check if an election is on going, set proper labels
        if (Election.GetExistingElectionStartDate() is None):
            self.labelElectionStatus.setText(_translate("Admin",
                                                        "<html><head/><body><p><span style=\" font-size:26pt;\">NO ELECTION STARTED YET</span></p></body></html>"))
        else:
            self.labelElectionStatus.setText(_translate("Admin", "<html><head/><body><p><span style=\" font-size:26pt;\">ELECTION ON GOING</span></p></body></html>"))

        self.label.setText(_translate("Admin", "TextLabel"))
        self.label_3.setText(_translate("Admin", "<html><head/><body><p>Candidate 1</p><p>Vote:</p></body></html>"))
        self.label_4.setText(_translate("Admin", "TextLabel"))
        self.label_5.setText(_translate("Admin", "<html><head/><body><p>Candidate 2:</p><p>Vote:</p></body></html>"))
        self.pushButtonCreateUser.clicked.connect(self.showCreateUser)
        self.pushButtonDeleteUser.clicked.connect(self.showDeleteUser)
        self.pushButtonEditUser.clicked.connect(self.showEditUser)
        self.pushButtonSummary.clicked.connect(self.showSummary)
        self.lineEditName.textChanged.connect(self.inputName)
        self.lineEditStudentNum.textChanged.connect(self.inputStudentNum)
        self.lineEditPass.textChanged.connect(self.inputPass)
        self.lineEditReenterPass.textChanged.connect(self.inputReenterPass)
        self.lineEditSearch.textChanged.connect(self.inputSearch)
        self.lineEditSearchEdit.textChanged.connect(self.inputSearchEdit)
        self.lineEdit.textChanged.connect(self.inputlineEdit)
        self.lineEdit_2.textChanged.connect(self.inputlineEdit_2)
        self.lineEdit_3.textChanged.connect(self.inputlineEdit_3)
        self.pushButtonCreate.clicked.connect(self.create)
        self.pushButtonStartElec.clicked.connect(self.startElec)
        self.pushButtonEndElec.clicked.connect(self.endElec)
        self.pushButtonDelete.clicked.connect(self.delete)
        self.pushButtonEdit.clicked.connect(self.edit)
        self.pushButtonSearch.clicked.connect(self.searchDelete)
        self.pushButtonSearchEdit.clicked.connect(self.searchEdit)
        
    def showCreateUser(self):
        self.scrollAreaCreateUser.show()
        self.scrollAreaDelete.hide()
        self.scrollAreaEdit.hide()
        self.scrollAreaSumm.hide()
    def showDeleteUser(self):
        self.scrollAreaCreateUser.hide()
        self.scrollAreaDelete.show()
        self.scrollAreaEdit.hide()
        self.scrollAreaSumm.hide()
    def showEditUser(self):
        self.scrollAreaCreateUser.hide()
        self.scrollAreaDelete.hide()
        self.scrollAreaEdit.show()
        self.scrollAreaSumm.hide()
    def showSummary(self):
        self.scrollAreaCreateUser.hide()
        self.scrollAreaDelete.hide()
        self.scrollAreaEdit.hide()
        self.scrollAreaSumm.show()
    def inputSearch(self):
        self.lineEditSearch.setStyleSheet("color: white")
        if self.lineEditSearch.text() == "":
            self.lineEditSearch.setStyleSheet("color: gray")
    def inputSearchEdit(self):
        self.lineEditSearchEdit.setStyleSheet("color: white")
        if self.lineEditSearchEdit.text() == "":
            self.lineEditSearchEdit.setStyleSheet("color: gray")
    def inputName(self):
        self.lineEditName.setStyleSheet("color: white")
        if self.lineEditName.text() == "":
            self.lineEditName.setStyleSheet("color: gray")
    def inputStudentNum(self):
        self.lineEditStudentNum.setStyleSheet("color: white")
        if self.lineEditStudentNum.text() == "":
            self.lineEditStudentNum.setStyleSheet("color: gray")
    def inputlineEdit(self):
        self.lineEdit.setStyleSheet("color: white")
        if self.lineEdit.text() == "":
            self.lineEdit.setStyleSheet("color: gray")
    def inputlineEdit_2(self):
        self.lineEdit_2.setStyleSheet("color: white")
        if self.lineEdit_2.text() == "":
            self.lineEdit_2.setStyleSheet("color: gray")
    def inputlineEdit_3(self):
        self.lineEdit_3.setStyleSheet("color: white")
        if self.lineEdit_3.text() == "":
            self.lineEdit_3.setStyleSheet("color: gray")
    def inputPass(self):
        self.lineEditPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPass.setStyleSheet("color: white")
        if self.lineEditPass.text() == "":
            self.lineEditPass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditPass.setStyleSheet("color: gray")  
    def inputReenterPass(self):
        self.lineEditReenterPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditReenterPass.setStyleSheet("color: white")
        if self.lineEditReenterPass.text() == "":
            self.lineEditReenterPass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.lineEditReenterPass.setStyleSheet("color: gray")

    #   DELETE EXISTING USER
    def delete(self):
        if (self.adminInterface.is_User()):

            if (self.adminInterface.is_user_admin()):
                failMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                   'Attempt to Delete Admin',
                                                   'You cannot delete an admin.',
                                                   QtWidgets.QMessageBox.Ok)
                failMsg.exec()
                self.adminInterface.reset_user()
                return

            #   ask for confirmation of deletion since this is will permanently lose the data
            #   distinguish between Candidate and User
            response = None
            if (self.adminInterface.is_Candidate()):
                confirmMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                   'Delete User?',
                                                   'This is not reversible, are you sure you want to delete this user?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                confirmMsg.setInformativeText('This user has been detected to be also a candidate.')
                response = confirmMsg.exec()
            else:
                confirmMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                   'Delete User?',
                                                   'This is not reversible, are you sure you want to delete this user?',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                response = confirmMsg.exec()
            if response == QtWidgets.QMessageBox.Yes:
                self.adminInterface.remove_user()
                self.adminInterface.reset_user()
                self.labelDelProfile.setText(
                    "<html><head/><body><p>"
                    "<span style=\" font-size:20pt;\">"
                    "Name: "
                    "</span>"
                    "</p>"
                    "<p>"
                    "<span style=\" font-size:20pt;\">"
                    "Student Number: "
                    "</span>"
                    "</p>"
                    "<p>"
                    "<span style=\" font-size:20pt;\">"
                    "Email: "
                    "</span>"
                    "</p>"
                    "</body>"
                    "</html>")
                successMsg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                               'User Deleted',
                                               'User successfully removed from database.',
                                               QtWidgets.QMessageBox.Ok)
                successMsg.show()

    #   EDIT EXISTING USER
    def edit(self):
        pass

    #   CREATE THE NEW USER PROFILE
    def create(self):
        pass

    #   SEARCH STUDENT NUMBER FROM DELETE
    def searchDelete(self):
        #   reset the current set user in AdminInterface first to prevent unexpected outputs
        self.adminInterface.reset_user()
        studId = self.lineEditSearch.text()
        try:
            studId = int(studId)
            self.adminInterface.set_user_userId(studId)

            if (self.adminInterface.is_User()):
                #   display in labels the user information
                user = self.adminInterface.GetUser()
                self.labelDelProfile.setText(
                    "<html><head/><body><p>"
                    "<span style=\" font-size:20pt;\">"
                    "Name: " + user.GetLastName() + ", " + user.GetFirstName() + " " + user.GetMidName() +
                    "</span>"
                    "</p>"
                    "<p>"
                    "<span style=\" font-size:20pt;\">"
                    "Student Number: " + (str)(user.GetUserId()) +
                    "</span>"
                    "</p>"
                    "<p>"
                    "<span style=\" font-size:20pt;\">"
                    "Email: " + user.GetEmail() +
                    "</span>"
                    "</p>"
                    "</body>"
                    "</html>")
            else:
                notFoundMsg = QtWidgets.QMessageBox()
                notFoundMsg.setIcon(QtWidgets.QMessageBox.Information)
                notFoundMsg.setText('User not found.')
                notFoundMsg.setWindowTitle('Search User')
                notFoundMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                notFoundMsg.exec()

        except ValueError:
            errorMsg = QtWidgets.QMessageBox()
            errorMsg.setIcon(QtWidgets.QMessageBox.Information)
            errorMsg.setText('Incorrect student number inputted.')
            errorMsg.setWindowTitle('Input Error')
            errorMsg.setStandardButtons(QtWidgets.QMessageBox.Ok)

            errorMsg.exec()

    #   SEARCH STUDENT NUMBER FROM EDIT
    def searchEdit(self):
        pass

    def startElec(self):
        self.labelElectionStatus.setText("<html><head/><body><p><span style=\" font-size:26pt;\">ELECTION ON GOING</span></p></body></html>")
        elecStartDate = datetime.now()
        electEndDate = elecStartDate + timedelta(days=self.election_duration)
        newElection = Election(elecStartDate, None)
        newElection.SetEndDate(electEndDate)

        newElection.StartElection()

    def endElec(self):
        self.labelElectionStatus.setText("<html><head/><body><p><span style=\" font-size:26pt;\">ELECTION ENDED</span></p></body></html>")
        Election.DropExistingElection()

    def PassAdminInfo(self, admin: Admin):
        self.user = admin
        self.adminInterface = AdminInterface(admin)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QWidget()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())