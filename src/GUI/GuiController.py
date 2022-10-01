from PyQt5.QtWidgets import QTableWidgetItem

from src.GUI.gui_ui import *
from src.GUI.SetStatesAndStatusWindow import *
from src.model.MealyAutomaton import *
from src.model.MooreAutomaton import *


MOORE_TYPE = "Automata de moore"
MEALY_TYPE = "Automata de mealy"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.sec = None
        self.automaton = None
        self.states = None
        self.stimulus = None
        self.responses = None
        self.type = None
        self.form = QtWidgets.QWidget()
        self.automatonTable.setItem(0, 0, QTableWidgetItem("A,3"))
        self.newAutomatonBt.clicked.connect(self.changesThings)

    def changesThings(self):
        if self.sec is None:
            self.sec = SetStatesAndStatusWindow()
        self.sec.setupUi(self.form, self)
        self.form.show()
        self.hide()

    def setAutomatonProperties(self, states: [], stimulus: [], automatonType):
        print(states)
        print(stimulus)
        print(automatonType)
        self.states = states
        self.stimulus = stimulus
        self.type = automatonType
