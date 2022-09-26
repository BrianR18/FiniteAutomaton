from abc import ABC

from automatonTools.FiniteAutomaton import FiniteAutomaton


class MealyAutomaton(FiniteAutomaton, ABC):

    def __init__(self, *args):
        super().__init__(*args)

    def addStateToMachine(self, state):
        self.__automaton.update({state: {}})

    def addStimulusAndResponseToState(self, state, stimulus, response):
        if stimulus not in self.__automaton:
            self.__automaton.get(state).update({stimulus: []})
        if len(self.__automaton.get(state).get(stimulus)) == 0:
            self.__automaton.get(state).get(stimulus).extend(response)

    def getEquivalentConnectAutomaton(self):
        if len(self.__automaton.keys()) > 1:  # There are more than one state
            self.__connected.append(self.__states[0])  # Add the initial state to connect set
            for stimulus in self.stimulus:
                stateToAdd = self.__automaton.get(self.__states[0]).get(stimulus)[0]
                if stateToAdd not in self.__connected:
                    self.__connected.append(stateToAdd)  # Add to connect set the states connect to the initial state
            self.__getStatesToCurrentState()
            if len(self.__connected) != len(self.__states):
                self.__deleteNotConnectedStates()

    def __getStatesToCurrentState(self):
        for state in self.__connected:
            if state != self.__states[0]:
                self.__connected.extend(self.__getConnectedWithCurrentState(state))

    def __deleteNotConnectedStates(self):
        for state in self.__states:
            if state not in self.__connected:
                self.__connected.pop(state)

    def __getConnectedWithCurrentState(self, state):
        connectedWithCurrentState = []
        for i in self.stimulus:
            stateToAdd = self.__automaton.get(state).get(i)[0]
            if stateToAdd not in connectedWithCurrentState and stateToAdd not in self.__connected:
                # Add to connect set the states connect to the initial state
                connectedWithCurrentState.append(stateToAdd)
        return connectedWithCurrentState


'''
{'A': {0: ['A', 0], 1: ['A', 0]}
'''
