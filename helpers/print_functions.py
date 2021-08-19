#print cube given cube
def print_cube(cube):
    print("            /-----------\\")
    for row in range(3):
        print("            |", cube[3 - 1][row], "|")
    print("/-----------o-----------o-----------------------\\")
    for row in range(3):
        print("|", end = " ")
        for face in [2, 1, 4, 6]:
            print(cube[face - 1][row], end =" | ")
        print("")
    print("\-----------o-----------o-----------------------/")
    for row in range(3):
        print("            |", cube[5 - 1][row], "|")
    print("            \-----------/")

# def print_cube_colored(cube):


#print face
def print_face(cube, face):
    for i in range(3):
        print(cube[face][i])

def print_line_break():
    print("========================================================================")