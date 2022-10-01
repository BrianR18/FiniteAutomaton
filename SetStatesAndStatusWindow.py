# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetStatesAndStatus.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class SetStatesAndStatusWindow(object):
    def __init__(self):
        self.Form = None
        self.mainW = None

    def setupUi(self, form, main):
        self.Form = form
        self.Form.setObjectName("Form")
        self.Form.resize(461, 195)
        self.mooreButton = QtWidgets.QRadioButton(self.Form)
        self.mooreButton.setGeometry(QtCore.QRect(300, 50, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mooreButton.setFont(font)
        self.mooreButton.setChecked(True)
        self.mooreButton.setObjectName("mooreButton")
        self.mealyButton = QtWidgets.QRadioButton(self.Form)
        self.mealyButton.setGeometry(QtCore.QRect(300, 70, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mealyButton.setFont(font)
        self.mealyButton.setObjectName("mealyButton")
        self.createButton = QtWidgets.QPushButton(self.Form)
        self.createButton.setGeometry(QtCore.QRect(300, 150, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.createButton.setFont(font)
        self.createButton.setObjectName("createButton")
        self.statesInput = QtWidgets.QPlainTextEdit(self.Form)
        self.statesInput.setGeometry(QtCore.QRect(20, 50, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statesInput.setFont(font)
        self.statesInput.setObjectName("statesInput")
        self.stimulusInput = QtWidgets.QPlainTextEdit(self.Form)
        self.stimulusInput.setGeometry(QtCore.QRect(20, 110, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stimulusInput.setFont(font)
        self.stimulusInput.setObjectName("stimulusInput")
        self.statesLabel = QtWidgets.QLabel(self.Form)
        self.statesLabel.setGeometry(QtCore.QRect(25, 30, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.statesLabel.setFont(font)
        self.statesLabel.setObjectName("statesLabel")
        self.stimulusStates = QtWidgets.QLabel(self.Form)
        self.stimulusStates.setGeometry(QtCore.QRect(25, 90, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stimulusStates.setFont(font)
        self.stimulusStates.setObjectName("stimulusStates")
        self.separatorInput = QtWidgets.QPlainTextEdit(self.Form)
        self.separatorInput.setGeometry(QtCore.QRect(300, 110, 25, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.separatorInput.setFont(font)
        self.separatorInput.setObjectName("separatorInput")
        self.separatorLabel = QtWidgets.QLabel(self.Form)
        self.separatorLabel.setGeometry(QtCore.QRect(330, 117, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.separatorLabel.setFont(font)
        self.separatorLabel.setObjectName("separatorLabel")
        self.retranslateUi(self.Form)
        self.mooreButton.setChecked(True)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        self.mainW = main
        self.createButton.clicked.connect(self.otra)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mooreButton.setText(_translate("Form", "Automata de moore"))
        self.mealyButton.setText(_translate("Form", "Automata de mealy"))
        self.createButton.setText(_translate("Form", "Crear máquina"))
        self.statesLabel.setText(_translate("Form", "Estados"))
        self.stimulusStates.setText(_translate("Form", "Estimulus"))
        self.separatorLabel.setText(_translate("Form", "Separador"))

    def otra(self):
        self.mainW.show()
        self.Form.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SetStatesAndStatusWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
