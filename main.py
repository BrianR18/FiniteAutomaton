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
    a = {"A": {}}
    a.get("A").update({0: []})
    a.get("A").get(0).append("A")
    a.get("A").get(0).append(1)
    a.get("A").update({1: []})
    a.get("A").get(1).append("B")
    a.get("A").get(1).append(1)
    a.update({"B": {}})
    a.get("B").update({0: []})
    a.get("B").get(0).append("B")
    a.get("B").get(0).append(1)
    a.get("B").update({1: []})
    a.get("B").get(1).append("A")
    a.get("B").get(1).append(0)
    print(a)
