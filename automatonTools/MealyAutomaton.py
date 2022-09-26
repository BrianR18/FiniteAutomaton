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
        connected = []
        if len(self.__automaton.keys()) > 1:
            for i in self.stimulus:
                if i not in connected:
                    connected.append(self.__automaton.get(i)[0])
            connected.append(self.__states[0])

    def __addToConnected(self, state):
        pass
