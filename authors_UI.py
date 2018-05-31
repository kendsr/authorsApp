# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authors.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(606, 537)
        self.lstAuthors = QtWidgets.QListWidget(Form)
        self.lstAuthors.setGeometry(QtCore.QRect(30, 60, 256, 192))
        self.lstAuthors.setObjectName("lstAuthors")
        self.lblAuthors = QtWidgets.QLabel(Form)
        self.lblAuthors.setGeometry(QtCore.QRect(30, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblAuthors.setFont(font)
        self.lblAuthors.setObjectName("lblAuthors")
        self.lstTitles = QtWidgets.QListWidget(Form)
        self.lstTitles.setGeometry(QtCore.QRect(330, 60, 256, 192))
        self.lstTitles.setObjectName("lstTitles")
        self.lblTitles = QtWidgets.QLabel(Form)
        self.lblTitles.setGeometry(QtCore.QRect(340, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblTitles.setFont(font)
        self.lblTitles.setObjectName("lblTitles")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Authors"))
        self.lblAuthors.setText(_translate("Form", "Authors"))
        self.lblTitles.setText(_translate("Form", "Titles"))

