from automatonTools import MealyAutomaton as at

blocks = {}

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



if __name__ == '__main__':
    automaton = at.MealyAutomaton(["A", "B", "C", "D", "E", "F", "G", "H", "J"], [0, 1], [0, 1])
    automaton.addStateToMachine("A")
    automaton.addStateToMachine("B")
    automaton.addStateToMachine("C")
    automaton.addStateToMachine("D")
    automaton.addStateToMachine("E")
    automaton.addStateToMachine("F")
    automaton.addStateToMachine("G")
    automaton.addStateToMachine("H")
    automaton.addStateToMachine("J")

    # automaton.addStateToMachine("E")
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
