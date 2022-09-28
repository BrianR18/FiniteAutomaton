from automatonTools import MealyAutomaton as at


if __name__ == '__main__':
    automaton = at.MealyAutomaton(["A", "B", "C", "D", "E"], [0, 1], [0, 1])
    automaton.addStateToMachine("A")
    automaton.addStateToMachine("B")
    automaton.addStateToMachine("C")
    automaton.addStateToMachine("D")
    automaton.addStateToMachine("E")
    # Formato de la función: estado, estimulo, respuesta: formato [EstadoAlQuellega, respuesta]
    automaton.addStimulusAndResponseToState("A", 0, ["A", 0])
    automaton.addStimulusAndResponseToState("A", 1, ["B", 0])
    automaton.addStimulusAndResponseToState("B", 0, ["A", 0])
    automaton.addStimulusAndResponseToState("B", 1, ["C", 1])
    automaton.addStimulusAndResponseToState("C", 0, ["C", 1])
    automaton.addStimulusAndResponseToState("C", 1, ["D", 0])
    automaton.addStimulusAndResponseToState("D", 0, ["D", 0])
    automaton.addStimulusAndResponseToState("D", 1, ["A", 0])
    automaton.addStimulusAndResponseToState("E", 0, ["A", 0])
    automaton.addStimulusAndResponseToState("E", 1, ["B", 1])
    print(automaton.automaton)
    '''
    Las insercciones anteriores generan la siguiente maquina de estados
    _|_0_|_1_
    A|A,0|B,0
    B|A,0|C,1
    C|C,1|D,0
    D|D,0|A,0
    E|A,1|B,1
    '''
    #automaton.getEquivalentConnectAutomaton()  # Al aplicar esta función al automata el Estado E se elimina de la máquina
    #print(automaton.automaton)
