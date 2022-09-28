from abc import ABC

from automatonTools.FiniteAutomaton import FiniteAutomaton


class MealyAutomaton(FiniteAutomaton, ABC):

    def __init__(self, *args):
        super().__init__(*args)

    def addStateToMachine(self, state):
        if state not in self.automaton.keys():
            self.automaton.update({state: {}})
        else:
            raise RuntimeError("Automaton already has the state " + str(state))

    def addStimulusAndResponseToState(self, state, stimulus, response: []):
        if stimulus not in self.automaton:
            self.automaton.get(state).update({stimulus: []})
        if len(self.automaton.get(state).get(stimulus)) == 0:
            self.automaton.get(state).get(stimulus).extend(response)

    def getEquivalentConnectAutomaton(self):
        if len(self.automaton.keys()) > 1:  # There are more than one state
            self.connected.append(self.states[0])  # Add the initial state to connect set
            for stimulus in self.stimulus:
                stateToAdd = self.automaton.get(self.states[0]).get(stimulus)[0]
                if stateToAdd not in self.connected:
                    self.connected.append(stateToAdd)  # Add to connect set the states connect to the initial state
            self.__getStatesToCurrentState()
            if len(self.connected) != len(self.states):
                self.__deleteNotConnectedStates()

    def __getStatesToCurrentState(self):
        for state in self.connected:
            if state != self.states[0]:
                self.connected.extend(self.__getConnectedWithCurrentState(state))

    def __deleteNotConnectedStates(self):
        for state in self.states:
            if state not in self.connected:
                self.automaton.pop(state)

    def __getConnectedWithCurrentState(self, state):
        connectedWithCurrentState = []
        for i in self.stimulus:
            stateToAdd = self.automaton.get(state).get(i)[0]
            if stateToAdd not in connectedWithCurrentState and stateToAdd not in self.connected:
                # Add to connect set the states connect to the initial state
                connectedWithCurrentState.append(stateToAdd)
        return connectedWithCurrentState

