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
    a = ["A", "B", "C"]
    for i in a:
        if i == "C":
            a.append("D")
        print(i)
