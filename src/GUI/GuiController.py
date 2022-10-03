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


def getListAsStr(linput: []):
    lstr = ""
    for element in linput:
        lstr = lstr + "," + element if len(lstr) == 1 else lstr + element
    return lstr


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
        self.automatonTable.clear()
        self.hide()

    def setAutomatonProperties(self, states: [], stimulus: [], responses: [], automatonType):
        self.states = states
        self.stimulus = stimulus
        self.type = automatonType
        self.responses = responses
        if automatonType == MOORE_TYPE:
            self.automaton = MooreAutomaton(states, stimulus, responses)
            aux = []
            aux.extend(stimulus)
            aux.append("Response")
            self.setColumns(aux)
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
            for column in range(len(self.stimulus)):
                z = self.states[row]
                x = {self.stimulus[column]: self.automatonTable.item(row, column).text()},
                c = self.automatonTable.item(row, len(self.stimulus)).text()
                self.automaton.addStimulusAndResponseToState(self.states[row],
                                                             {self.stimulus[column]:
                                                                  self.automatonTable.item(row, column).text()},
                                                             self.automatonTable.item(row, len(self.stimulus)).text())

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
        if self.type == MOORE_TYPE:
            aux = []
            aux.extend(self.automaton.stimulus)
            aux.append("Response")
            self.setColumns(aux)
        else:
            self.setColumns(self.automaton.stimulus)
        self.setRows(list(self.equivalentAutomaton.equivalent.automaton.keys()))
        self.putItems()

    def putItems(self):
        if self.type == MOORE_TYPE:
            self.putItemsToMoore()
        else:
            self.putItemsToMealy()

    def putItemsToMoore(self):
        matrix = self.equivalentAutomaton.equivalent.getElementsAsMatrix()
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                self.automatonTable.item(row, column).setText(str(matrix[row][column]))

    def putItemsToMealy(self):
        matrix = self.equivalentAutomaton.equivalent.getElementsAsMatrix()
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                self.automatonTable.item(row, column).setText(getListAsStr(matrix[row][column]))
