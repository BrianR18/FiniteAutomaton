# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generateAutomatonBt = QtWidgets.QPushButton(self.centralwidget)
        self.generateAutomatonBt.setGeometry(QtCore.QRect(410, 80, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
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
        self.automatonTable.setGeometry(QtCore.QRect(20, 20, 370, 311))
        self.automatonTable.setDragDropOverwriteMode(False)
        self.automatonTable.setShowGrid(True)
        self.automatonTable.setGridStyle(QtCore.Qt.DashDotLine)
        self.automatonTable.setCornerButtonEnabled(True)
        self.automatonTable.setObjectName("automatonTable")
        self.automatonTable.horizontalHeader().setDefaultSectionSize(60)
        self.newAutomatonBt = QtWidgets.QPushButton(self.centralwidget)
        self.newAutomatonBt.setGeometry(QtCore.QRect(410, 40, 121, 23))
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
