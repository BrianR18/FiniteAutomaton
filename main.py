import copy
from automatonTools import MealyAutomaton as me
from automatonTools import MooreAutomaton as mo
from automatonTools import FiniteAutomaton as fa

blocks = {}
automaton = fa.FiniteAutomaton()

def responsesAreEqual(u, v):
    for s in automaton.stimulus:
        if automaton.getResponse(u, s) != automaton.getResponse(v, s):
            return False
    return True

def createBlocks():
    added = []
    count = 0
    for u in automaton.states:
        if u not in added:
            count = count + 1
            blocks[u] = count
            added.append(u)
        for v in automaton.states:
            if u != v and v not in added:
                if responsesAreEqual(u, v):
                    blocks[v] = count
                    added.append(v)

def successorsAreInTheSameBlock(u, v):
    for s in automaton.stimulus:
        blockU = blocks[automaton.getSuccessorState(u, s)]
        blockV = blocks[automaton.getSuccessorState(v, s)]
        if blockU != blockV:
            return False
    return True

def iterateBlocks():
    while True:
        prev = copy.deepcopy(blocks)
        for u in blocks.keys():
            nextVal = max(blocks.values()) + 1
            for v in blocks.keys():
                if u != v and blocks[u] == blocks[v]:
                    if not successorsAreInTheSameBlock(u, v):
                        blocks[v] = nextVal
        if prev == blocks:
            return

def flipBlocksDict():
    flipped = {}
    for k, v in blocks.items():
        if v not in flipped:
            flipped[v] = [k]
        else:
            flipped[v].append(k)
    return flipped

def assignEquivalentStates():
    flippedDict = flipBlocksDict()
    equivalents = {}
    for i in blocks.keys():
        equivalents[i] = flippedDict[blocks[i]][0]
    return equivalents

def getEquivalentMealeyMachine():
    states = assignEquivalentStates()
    validStates = [*set(states.values())]
    validStates.remove(automaton.initialState())
    validStates.insert(0, automaton.initialState())
    eq = me.MealyAutomaton(validStates, automaton.stimulus, automaton.response)
    for u in validStates:
        eq.addStateToMachine(u)
    for u in eq.states:
        for s in automaton.stimulus:
            successor = states[automaton.getSuccessorState(u, s)]
            response = automaton.getResponse(u, s)
            eq.addStimulusAndResponseToState(u, s, [successor, response])
    return eq

def getEquivalentMooreMachine():
    states = assignEquivalentStates()
    validStates = [*set(states.values())]
    validStates.remove(automaton.initialState())
    validStates.insert(0, automaton.initialState())
    eq = mo.MooreAutomaton(validStates, automaton.stimulus, automaton.response)
    for u in validStates:
        eq.addStateToMachine(u)
    for u in eq.states:
        for s in automaton.stimulus:
            successor = states[automaton.getSuccessorState(u, s)]
            response = automaton.getActualStateResponse(u)
            eq.addStimulusAndResponseToState(u, {successor: s}, response)
    return eq

if __name__ == '__main__':
    #Mealy
    print("Mealy")
    automaton = me.MealyAutomaton(["A", "B", "C", "D", "E", "F", "G", "H", "J"], [0, 1], [0, 1])
    automaton.addStateToMachine("A")
    automaton.addStateToMachine("B")
    automaton.addStateToMachine("C")
    automaton.addStateToMachine("D")
    automaton.addStateToMachine("E")
    automaton.addStateToMachine("F")
    automaton.addStateToMachine("G")
    automaton.addStateToMachine("H")
    automaton.addStateToMachine("J")

    # Formato de la función: estado, estimulo, respuesta: formato [EstadoAlQuellega, respuesta]
    automaton.addStimulusAndResponseToState("A", 0, ["B", 0])
    automaton.addStimulusAndResponseToState("A", 1, ["C", 0])
    automaton.addStimulusAndResponseToState("B", 0, ["C", 1])
    automaton.addStimulusAndResponseToState("B", 1, ["D", 1])
    automaton.addStimulusAndResponseToState("C", 0, ["D", 0])
    automaton.addStimulusAndResponseToState("C", 1, ["E", 0])
    automaton.addStimulusAndResponseToState("D", 0, ["C", 1])
    automaton.addStimulusAndResponseToState("D", 1, ["B", 1])
    automaton.addStimulusAndResponseToState("E", 0, ["F", 1])
    automaton.addStimulusAndResponseToState("E", 1, ["E", 1])
    automaton.addStimulusAndResponseToState("F", 0, ["G", 0])
    automaton.addStimulusAndResponseToState("F", 1, ["C", 0])
    automaton.addStimulusAndResponseToState("G", 0, ["F", 1])
    automaton.addStimulusAndResponseToState("G", 1, ["G", 1])
    automaton.addStimulusAndResponseToState("H", 0, ["J", 1])
    automaton.addStimulusAndResponseToState("H", 1, ["B", 0])
    automaton.addStimulusAndResponseToState("J", 0, ["H", 1])
    automaton.addStimulusAndResponseToState("J", 1, ["D", 0])
    #automaton.getEquivalentConnectAutomaton()
    print(automaton.automaton)
    createBlocks()
    print(blocks)
    iterateBlocks()
    print(blocks)
    print(getEquivalentMealeyMachine().automaton)
    #Moore
    print("Moore")
    automaton = mo.MooreAutomaton(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"], [0, 1], [0, 1])
    automaton.addStateToMachine("A")
    automaton.addStateToMachine("B")
    automaton.addStateToMachine("C")
    automaton.addStateToMachine("D")
    automaton.addStateToMachine("E")
    automaton.addStateToMachine("F")
    automaton.addStateToMachine("G")
    automaton.addStateToMachine("H")
    automaton.addStateToMachine("I")
    automaton.addStateToMachine("J")
    automaton.addStateToMachine("K")
    automaton.addStimulusAndResponseToState("A", {0: "B"}, 0)
    automaton.addStimulusAndResponseToState("A", {1: "A"}, 0)
    automaton.addStimulusAndResponseToState("B", {0: "C"}, 0)
    automaton.addStimulusAndResponseToState("B", {1: "D"}, 0)
    automaton.addStimulusAndResponseToState("C", {0: "E"}, 0)
    automaton.addStimulusAndResponseToState("C", {1: "C"}, 0)
    automaton.addStimulusAndResponseToState("D", {0: "F"}, 0)
    automaton.addStimulusAndResponseToState("D", {1: "B"}, 0)
    automaton.addStimulusAndResponseToState("E", {0: "G"}, 0)
    automaton.addStimulusAndResponseToState("E", {1: "E"}, 0)
    automaton.addStimulusAndResponseToState("F", {0: "H"}, 0)
    automaton.addStimulusAndResponseToState("F", {1: "F"}, 0)
    automaton.addStimulusAndResponseToState("G", {0: "I"}, 0)
    automaton.addStimulusAndResponseToState("G", {1: "G"}, 0)
    automaton.addStimulusAndResponseToState("H", {0: "J"}, 0)
    automaton.addStimulusAndResponseToState("H", {1: "H"}, 0)
    automaton.addStimulusAndResponseToState("I", {0: "A"}, 1)
    automaton.addStimulusAndResponseToState("I", {1: "K"}, 1)
    automaton.addStimulusAndResponseToState("J", {0: "K"}, 0)
    automaton.addStimulusAndResponseToState("J", {1: "J"}, 0)
    automaton.addStimulusAndResponseToState("K", {0: "A"}, 1)
    automaton.addStimulusAndResponseToState("K", {1: "K"}, 1)
    print(automaton.automaton)
    createBlocks()
    iterateBlocks()
    print(blocks)
    print(getEquivalentMooreMachine().automaton)
