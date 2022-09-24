class FiniteAutomaton:

    def __init__(self, *args):
        self.__automaton = {}
        if len(args) == 0:
            self.__states = []
            self.__stimulus = []
            self.__response = []
        elif len(args) == 3:
            self.__states = args[0]
            self.__stimulus = args[1]
            self.__response = args[2]
        else:
            raise RuntimeError("Invalid number of arguments")

    @property
    def states(self):
        return self.__states

    @property
    def stimulus(self):
        return self.__stimulus

    @property
    def response(self):
        return self.__response

    @property
    def automaton(self):
        return self.__automaton

    @states.setter
    def states(self, new_states):
        self.__states = new_states

    @stimulus.setter
    def stimulus(self, new_stimulus):
        self.__stimulus = new_stimulus

    @response.setter
    def response(self, new_response):
        self.__response = new_response

    @automaton.setter
    def automaton(self, new_automaton):
        self.__automaton = new_automaton

    def addState(self, state, transition, *response):
        if len(response) == 0:
            self.__automaton.update({state: {}})

'''
a.update({"B": {}})
    a.get("B").update({0: []})
    a.get("B").get(0).append("B")
    a.get("B").get(0).append(1)
'''