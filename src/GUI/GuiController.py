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
        self.states = None
        self.stimulus = None
        self.automaton = None
        self.responses = None
        self.type = None
        self.form = QtWidgets.QWidget()
        self.automatonTable.setItem(0, 0, QTableWidgetItem("A,3"))
        self.newAutomatonBt.clicked.connect(self.changesThings)
        self.generateAutomatonBt.clicked.connect(self.generateAutomatonConnectedAndMinimum)

    def changesThings(self):
        if self.sec is None:
            self.sec = SetStatesAndStatusWindow()
        self.sec.setupUi(self.form, self)
        self.form.show()
        self.hide()

    def setAutomatonProperties(self, states: [], stimulus: [], automatonType):
        self.states = states
        self.stimulus = stimulus
        self.type = automatonType
        if automatonType == MOORE_TYPE:
            stimulus.append("Response")
            self.automaton = MooreAutomaton(states, stimulus)
        else:
            self.automaton = MealyAutomaton(states, stimulus)
        self.setColumns(stimulus)
        self.setRows(states)

    def setStimulusAndResponse(self):
        for row in range(len(self.states)):
            for column in range(len(self.stimulus)):
                response = self.automatonTable.item(row, column).text().split(",")
                self.automaton.addStimulusAndResponseToState(self.states[row], self.stimulus[column], response)

    def generateAutomatonConnectedAndMinimum(self):
        for state in self.states:
            self.automaton.addStateToMachine(state)
        self.setStimulusAndResponse()
        self.automaton.getEquivalentConnectAutomaton()

