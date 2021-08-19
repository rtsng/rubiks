import random
import math
'''
cube[1]
0 -> 1 -> 2 -> 5 -> 8 -> 7 -> 6 -> 3 -> 0

cube[2] 2 5 8 -> cube [3] 6 7 8 -> cube [4] 0 3 6 -> cube[5] 0 1 2 -> cube[2] 2 5 8
'''

def rotateface(face, cube, clockwise):
    if clockwise:
        m = cube[face]
        cube[face] = [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]
        return cube
    else:
        m = cube[face]
        cube[face] = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
        return cube


def do_f(cube):
    cube = rotateface(0, cube, True)
    temparr = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]

    cube[1][0][2] = cube[4][0][0]
    cube[1][1][2] = cube[4][0][1]
    cube[1][2][2] = cube[4][0][2]

    cube[4][0][0] = cube[3][2][0]
    cube[4][0][1] = cube[3][1][0]
    cube[4][0][2] = cube[3][0][0]

    cube[3][2][0] = cube[2][2][2]
    cube[3][1][0] = cube[2][2][1]
    cube[3][0][0] = cube[2][2][0]

    cube[2][2][0] = temparr[2]
    cube[2][2][1] = temparr[1]
    cube[2][2][2] = temparr[0]
    return cube

def do_fprime(cube):
    return do_f(do_f(do_f(cube)))
 
def do_r(cube):
    cube = rotateface(3, cube, True)
    temparr = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]

    cube[0][0][2] = cube[4][0][2]
    cube[0][1][2] = cube[4][1][2]
    cube[0][2][2] = cube[4][2][2]

    cube[4][0][2] = cube[5][2][0]
    cube[4][1][2] = cube[5][1][0]
    cube[4][2][2] = cube[5][0][0]

    cube[5][0][0] = cube[2][2][2]
    cube[5][1][0] = cube[2][1][2]
    cube[5][2][0] = cube[2][0][2]

    cube[2][0][2] = temparr[0]
    cube[2][1][2] = temparr[1]
    cube[2][2][2] = temparr[2]
    return cube

def do_rprime(cube):
    return do_r(do_r(do_r(cube)))

def do_l(cube):
    cube = rotateface(1, cube, True)
    temparr = [cube[4][0][0], cube[4][1][0], cube[4][2][0]]

    cube[4][0][0] = cube[0][0][0]
    cube[4][1][0] = cube[0][1][0]
    cube[4][2][0] = cube[0][2][0]

    cube[0][0][0] = cube[2][0][0]
    cube[0][1][0] = cube[2][1][0]
    cube[0][2][0] = cube[2][2][0]

    cube[2][0][0] = cube[5][2][2]
    cube[2][1][0] = cube[5][1][2]
    cube[2][2][0] = cube[5][0][2]

    cube[5][2][2] = temparr[0]
    cube[5][1][2] = temparr[1]
    cube[5][0][2] = temparr[2]
    return cube

def do_lprime(cube):
    return do_l(do_l(do_l(cube)))

def do_u(cube):
    cube = rotateface(2, cube, True)
    temparr = [cube[0][0][0], cube[0][0][1], cube[0][0][2]]

    cube[0][0][0] = cube[3][0][0]
    cube[0][0][1] = cube[3][0][1]
    cube[0][0][2] = cube[3][0][2]

    cube[3][0][0] = cube[5][0][0]
    cube[3][0][1] = cube[5][0][1]
    cube[3][0][2] = cube[5][0][2]

    cube[5][0][0] = cube[1][0][0]
    cube[5][0][1] = cube[1][0][1]
    cube[5][0][2] = cube[1][0][2]

    cube[1][0][0] = temparr[0]
    cube[1][0][1] = temparr[1]
    cube[1][0][2] = temparr[2]
    return cube

def do_uprime(cube):
    return do_u(do_u(do_u(cube)))

def do_d(cube):
    cube = rotateface(4, cube, True)
    # print_cube(cube)
    temparr = [cube[0][2][0], cube[0][2][1], cube[0][2][2]]

    cube[0][2][0] = cube[1][2][0]
    cube[0][2][1] = cube[1][2][1]
    cube[0][2][2] = cube[1][2][2]

    cube[1][2][0] = cube[5][2][0]
    cube[1][2][1] = cube[5][2][1]
    cube[1][2][2] = cube[5][2][2]

    cube[5][2][0] = cube[3][2][0]
    cube[5][2][1] = cube[3][2][1]
    cube[5][2][2] = cube[3][2][2]

    cube[3][2][0] = temparr[0]
    cube[3][2][1] = temparr[1]
    cube[3][2][2] = temparr[2]
    return cube

def do_dprime(cube):
    return do_d(do_d(do_d(cube)))

def do_b(cube):
    cube = rotateface(5, cube, True)
    # print_cube(cube)
    temparr = [cube[2][0][0], cube[2][0][1], cube[2][0][2]]

    cube[2][0][0] = cube[3][0][2]
    cube[2][0][1] = cube[3][1][2]
    cube[2][0][2] = cube[3][2][2]

    cube[3][0][2] = cube[4][2][2]
    cube[3][1][2] = cube[4][2][1]
    cube[3][2][2] = cube[4][2][0]

    cube[4][2][2] = cube[1][2][0]
    cube[4][2][1] = cube[1][1][0]
    cube[4][2][0] = cube[1][0][0]

    cube[1][2][0] = temparr[0]
    cube[1][1][0] = temparr[1]
    cube[1][0][0] = temparr[2]
    return cube

def do_bprime(cube):
    return do_b(do_b(do_b(cube)))

def execute_moves(cube, moves):
    move_array = moves.split()
    for i in move_array:
        if i == "r":
            cube = do_r(cube)
        elif i == "u":
            cube = do_u(cube)    
        elif i == "l":
            cube = do_l(cube) 
        elif i == "d":
            cube = do_d(cube) 
        elif i == "f":
            cube = do_f(cube) 
        elif i == "b":
            cube = do_b(cube) 
        elif i == "r'":
            cube = do_rprime(cube)
        elif i == "u'":
            cube = do_uprime(cube)    
        elif i == "l'":
            cube = do_lprime(cube) 
        elif i == "d'":
            cube = do_dprime(cube) 
        elif i == "f'":
            cube = do_fprime(cube) 
        elif i == "b'":
            cube = do_bprime(cube) 
    return cube

def scramble_cube(cube):
    move_list = ["r", "d", "u", "f", "u", "b", "r'", "d'", "u'", "f'", "u'", "b'"]
    arr = []
    
    for i in range(20):
        arr.append(int(math.floor(random.uniform(0,11.99999999))))
    
    scramble = ""

    for i in arr:
        scramble += " " + move_list[i]

    print("scramble: " + scramble)
    return execute_moves(cube, scramble)
