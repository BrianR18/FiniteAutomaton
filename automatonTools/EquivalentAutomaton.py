import copy
import FiniteAutomaton.automatonTools.MealyAutomaton as me
import FiniteAutomaton.automatonTools.MooreAutomaton as mo


class EquivalentAutomaton:

    def __init__(self, automaton):
        self.__blocks = {}
        self.__automaton = automaton
        self.__equivalent = None

    @property
    def automaton(self):
        return self.__automaton

    @property
    def equivalent(self):
        return self.__equivalent

    def __responsesAreEqual(self, u, v):
        for s in self.__automaton.stimulus:
            if self.__automaton.getResponse(u, s) != self.__automaton.getResponse(v, s):
                return False
        return True

    def __createBlocks(self):
        added = []
        count = 0
        for u in self.__automaton.states:
            if u not in added:
                count = count + 1
                self.__blocks[u] = count
                added.append(u)
            for v in self.__automaton.states:
                if u != v and v not in added:
                    if self.__responsesAreEqual(u, v):
                        self.__blocks[v] = count
                        added.append(v)

    def __successorsAreInTheSameBlock(self, u, v):
        for s in self.__automaton.stimulus:
            blockU = self.__blocks[self.__automaton.getSuccessorState(u, s)]
            blockV = self.__blocks[self.__automaton.getSuccessorState(v, s)]
            if blockU != blockV:
                return False
        return True

    def __iterateBlocks(self):
        while True:
            prev = copy.deepcopy(self.__blocks)
            for u in self.__blocks.keys():
                nextVal = max(self.__blocks.values()) + 1
                for v in self.__blocks.keys():
                    if u != v and self.__blocks[u] == self.__blocks[v]:
                        if not self.__successorsAreInTheSameBlock(u, v):
                            self.__blocks[v] = nextVal
            if prev == self.__blocks:
                return

    def __flipBlocksDict(self):
        flipped = {}
        for k, v in self.__blocks.items():
            if v not in flipped:
                flipped[v] = [k]
            else:
                flipped[v].append(k)
        return flipped

    def __assignEquivalentStates(self):
        flippedDict = self.__flipBlocksDict()
        equivalents = {}
        for i in self.__blocks.keys():
            equivalents[i] = flippedDict[self.__blocks[i]][0]
        return equivalents

    def __getEquivalentMealeyMachine(self):
        states = self.__assignEquivalentStates()
        validStates = [*set(states.values())]
        validStates.remove(self.__automaton.initialState())
        validStates.insert(0, self.__automaton.initialState())
        eq = me.MealyAutomaton(validStates, self.__automaton.stimulus, self.__automaton.response)
        for u in validStates:
            eq.addStateToMachine(u)
        for u in eq.states:
            for s in self.__automaton.stimulus:
                successor = states[self.__automaton.getSuccessorState(u, s)]
                response = self.__automaton.getResponse(u, s)
                eq.addStimulusAndResponseToState(u, s, [successor, response])
        self.__equivalent = eq

    def __getEquivalentMooreMachine(self):
        states = self.__assignEquivalentStates()
        validStates = [*set(states.values())]
        validStates.remove(self.__automaton.initialState())
        validStates.insert(0, self.__automaton.initialState())
        eq = mo.MooreAutomaton(validStates, self.__automaton.stimulus, self.__automaton.response)
        for u in validStates:
            eq.addStateToMachine(u)
        for u in eq.states:
            for s in self.__automaton.stimulus:
                successor = states[self.__automaton.getSuccessorState(u, s)]
                response = self.__automaton.getActualStateResponse(u)
                eq.addStimulusAndResponseToState(u, {successor: s}, response)
        self.__equivalent = eq

    def proccessEquivalentAutomaton(self):
        self.__createBlocks()
        self.__iterateBlocks()
        if type(self.__automaton) is me.MealyAutomaton:
            self.__getEquivalentMealeyMachine()
        else:
            self.__getEquivalentMooreMachine()
