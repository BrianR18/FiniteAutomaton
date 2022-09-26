def readFile():
    content = ""
    with open("./files/testFile.csv") as file:
        cont = True
        while cont:
            line = file.readline()
            cont = line != ""
            content += line + "\n" if line != "" else ""
    return content


if __name__ == '__main__':
    b = ["A", "B", "C"]
    a = {}
    connected = []
    for i in b:
        a.update({i: {}})
        a.get(i).update({0: []})
        a.get(i).get(0).extend([i, 0])
        a.get(i).update({1: []})
        a.get(i).get(1).extend([i, 0])
    stimulus = [0, 1]  # {0: ['A', 0], 1: ['A', 0]}
    for i in stimulus:  # {'A': {0: ['A', 0], 1: ['A', 0]} }
        connected.append(a.get("A").get(i)[0])
    print(connected)
