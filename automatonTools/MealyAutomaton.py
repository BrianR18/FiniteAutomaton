from abc import ABC

from automatonTools.FiniteAutomaton import FiniteAutomaton


class MealyAutomaton(FiniteAutomaton, ABC):

    def __init__(self, *args):
        super().__init__(*args)

    def addStimulusAndResponseToState(self, state, stimulus, response):
        if stimulus not in self.__automaton:
            self.__automaton.get(state).update({stimulus: []})
        self.__automaton.get(state).get(stimulus).extend(response)
