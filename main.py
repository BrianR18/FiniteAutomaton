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
    a = {"Brian": []}
    a.get("Brian").extend(["A", 1])
    print(a)
    a = {"Brian": []}
    a.get("Brian").append(["A", 1])
    print(a)
    a = {"Brian": []}

