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
        Form.resize(863, 537)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lblAuthors = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblAuthors.setFont(font)
        self.lblAuthors.setObjectName("lblAuthors")
        self.gridLayout.addWidget(self.lblAuthors, 0, 0, 1, 1)
        self.lblTitles = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblTitles.setFont(font)
        self.lblTitles.setObjectName("lblTitles")
        self.gridLayout.addWidget(self.lblTitles, 0, 1, 1, 1)
        self.lstAuthors = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lstAuthors.setFont(font)
        self.lstAuthors.setObjectName("lstAuthors")
        self.gridLayout.addWidget(self.lstAuthors, 1, 0, 1, 1)
        self.lstTitles = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lstTitles.setFont(font)
        self.lstTitles.setObjectName("lstTitles")
        self.gridLayout.addWidget(self.lstTitles, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Authors"))
        self.lblAuthors.setText(_translate("Form", "Authors"))
        self.lblTitles.setText(_translate("Form", "Titles"))

