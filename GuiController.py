from PyQt5.QtWidgets import QTableWidgetItem

import MealyAutomaton as me
import MooreAutomaton as mo
from gui_ui import *
from SetStatesAndStatusWindow import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.sec = None
        self.form = QtWidgets.QWidget()
        self.automatonTable.setItem(0, 0, QTableWidgetItem("A,3"))
        self.newAutomatonBt.clicked.connect(self.changesThings)

    def changesThings(self):
        if self.sec is None:
            self.sec = SetStatesAndStatusWindow()
        self.sec.setupUi(self.form, self)
        self.form.show()
        self.hide()
