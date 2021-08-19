from helpers.print_functions import print_cube, print_line_break
from helpers.rotate import *
from helpers.get_cube import solved_cube, solved_cube_colored

# for reference the faces are refered to as such

#       |---|
#       | 3 |
#   |---|---|---|---| 
#   | 2 | 1 | 4 | 6 |
#   |---|---|---|---|
#       | 5 |
#       |---|

# where 1 is the face you are looking at.

# consider the case where you are looking at the white face witht he green face down
# 1 - white
# 2 - orange
# 3 - blue
# 4 - red
# 5 - green
# 6 - yellow



# cube = do_f(cube)

# while cube != solved_cube():
#     print("here!")
#     cube = do_f(cube)

cube = solved_cube()
print_line_break()
print("scramble: r u u b' d u' u' f u' b' d u' r r u' d' f' u' f f'")
print_line_break()
cube = execute_moves(cube,"r u u b' d u' u' f u' b' d u' r r u' d' f' u' f f'")
print_cube(cube)
print_line_break()
cube = execute_moves(cube,"f f' u f d u r' r' u d' b u f' u u d' b u' u' r'")
print_cube(cube)



