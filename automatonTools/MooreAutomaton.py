from abc import ABC

from automatonTools.FiniteAutomaton import FiniteAutomaton


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

'''
a = {"A": [{}]}
    a.get("A").append(0)
    print(a)
    a.get("A")[0].update({0: "D"})
    a.get("A")[0].update({1: "B"})
    a.update({"B": [{}]})
    a.get("B").append(1)
'''