def readsave():

    # it reads the "save.txt" file and returns the board condition

    a = []
    with open("save.txt", "r") as file:
        lines = file.readlines()[2:12]
        a.append(int(lines[0].strip()))
        for line in lines[2:10]:
            state = line.strip()
            a.append(list(map(int, state.split())))
    return a


def writesave(state, color):
    
    # after coin is placed it writes the state of board to "save.txt"

    with open("save.txt", "r") as file:
        lines = file.readlines()[0:4]

    lines[2] = str(color) + "\n"
    for i in state:
        s = " ".join(map(str, i)) + "\n"
        lines.append(s)

    with open("save.txt", "w") as file:
        file.writelines(lines)


def resetsave():
    
    # it returns the initial state of board
    
    state = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 0, 1, -1, -1, -1],
        [-1, -1, -1, 1, 0, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]
    writesave(state, 1)