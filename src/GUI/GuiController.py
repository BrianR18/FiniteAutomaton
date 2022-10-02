from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from src.GUI.gui_ui import *
from src.GUI.SetStatesAndStatusWindow import *
from src.model.MealyAutomaton import *
from src.model.MooreAutomaton import *
from src.model.EquivalentAutomaton import *
import threading

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
        self.equivalentAutomaton = None
        self.form = QtWidgets.QWidget()
        self.newAutomatonBt.clicked.connect(self.changesThings)
        self.generateAutomatonBt.clicked.connect(self.generateAutomatonConnectedAndMinimum)

    def changesThings(self):
        if self.sec is None:
            self.sec = SetStatesAndStatusWindow()
        self.sec.setupUi(self.form, self)
        self.form.show()
        self.hide()

    def setAutomatonProperties(self, states: [], stimulus: [], responses: [], automatonType):
        self.states = states
        self.stimulus = stimulus
        self.type = automatonType
        self.responses = responses
        if automatonType == MOORE_TYPE:
            stimulus.append("Response")
            self.automaton = MooreAutomaton(states, stimulus, responses)
        else:
            self.automaton = MealyAutomaton(states, stimulus, responses)
        self.setColumns(stimulus)
        self.setRows(states)

    def setStimulusAndResponseMealy(self):
        for row in range(len(self.states)):
            for column in range(len(self.stimulus)):
                response = self.automatonTable.item(row, column).text().split(",")
                self.automaton.addStimulusAndResponseToState(self.states[row], self.stimulus[column], response)

    def setStimulusAndResponseMoore(self):
        for row in range(len(self.states)):
            for column in range(len(self.stimulus) - 1):
                self.automaton.addStimulusAndResponseToState(self.states[row],
                                                             {self.stimulus[column],
                                                              self.automatonTable.item(row, column).text()},
                                                             self.automatonTable.item(row, len(self.stimulus) - 1).text())

    def generateAutomatonConnectedAndMinimum(self):
        for state in self.states:
            self.automaton.addStateToMachine(state)
        if self.type == MOORE_TYPE:
            self.setStimulusAndResponseMoore()
        else:
            self.setStimulusAndResponseMealy()
        self.equivalentAutomaton = EquivalentAutomaton(self.automaton)
        equivalentThread = threading.Thread(target=self.setNewAutomaton)
        equivalentThread.start()  # D

    def setNewAutomaton(self):
        self.equivalentAutomaton.processReducedAutomaton()
        self.setColumns(self.automaton.stimulus)
        self.setRows(list(self.equivalentAutomaton.equivalent.automaton.keys()))
