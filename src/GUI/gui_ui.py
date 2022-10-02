# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

MAX_COLUMN_SIZE = 300
MIN_COLUMN_SIZE = 60
MAX_ROW_SIZE = 325


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 370)
        MainWindow.setMaximumSize(510, 370)
        MainWindow.setMinimumSize(510, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generateAutomatonBt = QtWidgets.QPushButton(self.centralwidget)
        self.generateAutomatonBt.setGeometry(QtCore.QRect(360, 80, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)  # 10 / 5
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateAutomatonBt.sizePolicy().hasHeightForWidth())
        self.generateAutomatonBt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.generateAutomatonBt.setFont(font)
        self.generateAutomatonBt.setMouseTracking(False)
        self.generateAutomatonBt.setTabletTracking(False)
        self.generateAutomatonBt.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.generateAutomatonBt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.generateAutomatonBt.setAutoFillBackground(False)
        self.generateAutomatonBt.setDefault(False)
        self.generateAutomatonBt.setObjectName("generateAutomatonBt")
        self.automatonTable = QtWidgets.QTableWidget(self.centralwidget)
        self.automatonTable.setGeometry(QtCore.QRect(20, 20, 320, 325))
        self.automatonTable.setDragDropOverwriteMode(False)
        self.automatonTable.setShowGrid(True)
        self.automatonTable.setGridStyle(QtCore.Qt.DashDotLine)
        self.automatonTable.setCornerButtonEnabled(True)
        self.automatonTable.setObjectName("automatonTable")
        self.newAutomatonBt = QtWidgets.QPushButton(self.centralwidget)
        self.newAutomatonBt.setGeometry(QtCore.QRect(360, 40, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.newAutomatonBt.setFont(font)
        self.newAutomatonBt.setObjectName("newAutomatonBt")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generateAutomatonBt.setText(_translate("MainWindow", "Generar autómata \n"
                                                                  "mínimo equivalente"))
        self.automatonTable.setSortingEnabled(False)
        self.newAutomatonBt.setText(_translate("MainWindow", "Nuevo autómata"))

    def setColumns(self, labels: []):
        if len(labels) >= 5:
            self.automatonTable.horizontalHeader().setMaximumSectionSize(MIN_COLUMN_SIZE)
            self.automatonTable.horizontalHeader().setMinimumSectionSize(MIN_COLUMN_SIZE)
        else:
            self.automatonTable.horizontalHeader().setMaximumSectionSize(math.floor(MAX_COLUMN_SIZE / len(labels)))
            self.automatonTable.horizontalHeader().setMinimumSectionSize(math.floor(MAX_COLUMN_SIZE / len(labels)))
            self.automatonTable.horizontalHeader().setDefaultSectionSize(math.floor(MAX_COLUMN_SIZE / len(labels)))
        self.automatonTable.setColumnCount(len(labels))
        self.automatonTable.setHorizontalHeaderLabels(labels)

    def setRows(self, labels: []):
        self.automatonTable.setRowCount(len(labels))
        self.automatonTable.setVerticalHeaderLabels(labels)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
