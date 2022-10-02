from abc import ABC
from src.model.FiniteAutomaton import FiniteAutomaton


class MooreAutomaton(FiniteAutomaton, ABC):

    def __init__(self, *args):
        super().__init__(*args)

    def addStateToMachine(self, state):
        if state not in self.automaton.keys():
            self.automaton.update({state: [{}]})
        else:
            raise RuntimeError("Automaton already has the state " + str(state))

    def addStimulusAndResponseToState(self, state, stimulus: {}, response):
        if len(self.automaton.get(state)) == 1:  # Checks if the current state doesn't have a response yet
            self.automaton.get(state).append(response)  # Add the responses to the current state
        (self.automaton.get(state))[0].update(stimulus)

    def getActualStateResponse(self, state):
        return self.automaton.get(state)[1]

    def getResponse(self, state, stimulus):
        return self.automaton.get(self.getSuccessorState(state, stimulus))[1]

    def getSuccessorState(self, start, stimulus):
        return self.automaton.get(start)[0][stimulus]

    def getEquivalentConnectAutomaton(self):
        if len(self.automaton.keys()) > 1:  # There are more than one state
            self.connected.append(self.initialState())  # Add the initial state to connect set
            for stimulus in self.stimulus:
                stateToAdd = self.getSuccessorState(self.initialState(), stimulus)
                if stateToAdd not in self.connected:
                    self.connected.append(stateToAdd)  # Add to connect set the states connect to the initial state
            self.__getStatesToCurrentState()
            if len(self.connected) != len(self.states):
                self.__deleteNotConnectedStates()
                aux = self.automaton.keys()
                self.states = []
                for state in aux:
                    self.states.append(state)

    def __getStatesToCurrentState(self):
        for state in self.connected:
            if state != self.initialState():
                self.connected.extend(self.__getConnectedWithCurrentState(state))

    def __deleteNotConnectedStates(self):
        for state in self.states:
            if state not in self.connected:
                self.automaton.pop(state)

    def __getConnectedWithCurrentState(self, state):
        connectedWithCurrentState = []
        for i in self.stimulus:
            stateToAdd = self.getSuccessorState(state, i)
            if stateToAdd not in connectedWithCurrentState and stateToAdd not in self.connected:
                # Add to connect set the states connect to the initial state
                connectedWithCurrentState.append(stateToAdd)
        return connectedWithCurrentState
