import copy
import src.model.MealyAutomaton as me
import src.model.MooreAutomaton as mo


class EquivalentAutomaton:
    """
    The class that provides the methods to reduce a finite state automaton
    whether it is a Mealy automaton or a Moore automaton.
    Defines the blocks, automaton and equivalent attributes.
      |  - automaton saves the given automaton to reduce.
      |  - equivalent saves the equivalent reduced automaton.
      |  - blocks refers to the partitions used to determine the equivalent states. We use a dictionary where the key is a state of the automaton and the value is the block where the state is located.
    """

    def __init__(self, automaton):
        """
        Constructor for the Equivalent Automaton class. Requires as param the automaton to reduce.
        Defines the blocks, automaton and equivalent attributes.
        :param automaton: the given automaton to reduce. It must be an instance of a MealyAutomaton or a MooreAutomaton
        """
        if not isinstance(automaton, (me.MealyAutomaton, mo.MooreAutomaton)):
            raise RuntimeError("automaton must be moore or mealy")
        self.__blocks = {}
        self.__automaton = automaton
        self.__equivalent = None

    @property
    def automaton(self):
        """
        Getter for the automaton attribute
        :return: the given automaton to reduce
        """
        return self.__automaton

    @property
    def equivalent(self):
        """
        Getter for the equivalent attribute
        :return: the reduced equivalent automaton
        """
        return self.__equivalent

    def __responsesAreEqual(self, u, v):
        """
        Determines whether two given states give the same response for each stimulus on the automaton
        :param u: one of the states
        :param v: the other state
        :return: True if the two states have the same response for each stimulus. False if not
        """
        for s in self.__automaton.stimulus:
            if self.__automaton.getResponse(u, s) != self.__automaton.getResponse(v, s):
                return False
        return True

    def __createBlocks(self):
        """
        Creates the first partition P1. Adds the state that have the same response for each state in the same block.
        The states are in the same block if they have the same value.
        """
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
        """
        Determines if the successors of two given states are in the same block of the current partition
        :param u: the first state
        :param v: the second state
        :return: True if the successors are in the same block. False if not
        """
        for s in self.__automaton.stimulus:
            blockU = self.__blocks[self.__automaton.getSuccessorState(u, s)]
            blockV = self.__blocks[self.__automaton.getSuccessorState(v, s)]
            if blockU != blockV:
                return False
        return True

    def __iterateBlocks(self):
        """
        Iterates over the blocks of the partition to create the next partitions.
        Stops when the current transition equals the previous transition
        """
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
        """
        Flips the partitions blocks dictionary.
        For the key we have the number of the block.
        For the value we have the list of the states that are in the same block of the final partition hence
        being equivalent
        :return: the flipped dictionary of the blocks
        """
        flipped = {}
        for k, v in self.__blocks.items():
            if v not in flipped:
                flipped[v] = [k]
            else:
                flipped[v].append(k)
        return flipped

    def __assignEquivalentStates(self):
        """
        Determines the new name for the states of the new reduced automaton.
        Chooses the first state present in the block of the final partition as the one that represents
        the others in the list
        :return: the new dictionary of states. key: the number of the block. value: the state that represents that block
        """
        flippedDict = self.__flipBlocksDict()
        equivalents = {}
        for i in self.__blocks.keys():
            equivalents[i] = flippedDict[self.__blocks[i]][0]
        return equivalents

    def __getEquivalentMealeyMachine(self):
        """
        Creates the new equivalent automaton for a Mealy automaton
        :return: the new reduced equivalent automaton
        """
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
        """
        Creates the new equivalent automaton for a Moore automaton
        :return: the new reduced equivalent automaton
        """
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

    def processReducedAutomaton(self):
        """
        Calls the other methods to process the given automaton and get the equivalent reduced automaton
        :return: the new reduced automaton after processing the given automaton
        """
        self.__automaton.getEquivalentConnectAutomaton()
        self.__createBlocks()
        self.__iterateBlocks()
        if isinstance(self.__automaton, me.MealyAutomaton):
            self.__getEquivalentMealeyMachine()
        else:
            self.__getEquivalentMooreMachine()
