import kociemba
from . import validate

def transform_format(moves):
    result = []
    for move in moves:
        move = move.lower()
        if "2" in move:
            move_without_2 = move.replace("2", "")
            result.extend([move_without_2] * 2)
        else:
            result.append(move)
    return result


def kociemba_solve(rubiks_cube):
    sequence = []
    # turn the rubiks notation to kociemba compatible notation

    solvable,error=validate.checkCube(rubiks_cube)
    if solvable==False:return [],False,error

    # 1 take the centers of the cube
    color_to_notation = {
        rubiks_cube["B5"]: "B",
        rubiks_cube["U5"]: "U",
        rubiks_cube["F5"]: "F",
        rubiks_cube["L5"]: "L",
        rubiks_cube["R5"]: "R",
        rubiks_cube["D5"]: "D",
    }
    order = ["U", "R", "F", "D", "L", "B"]
    kociemba_string = ""
    # 2 compare the centers with all the elements of the dictionary and map the cubes accordingly
    for face in order:
        for no in range(1, 10):
            # makes position for the cube to iterate through in order
            position = f"{face}{no}"

            color = rubiks_cube[position]
            # gets the required notation for the color
            color_to_notation[color]
            kociemba_string = kociemba_string + color_to_notation[color]
    try:
        solution = kociemba.solve(kociemba_string)
        sequence_kociemba_format = solution.split(" ")

        # remote the 2 at the end to make it two different moves
        sequence = transform_format(sequence_kociemba_format)
        is_solved = True
        error = ""
    except Exception as e:
        sequence = []
        is_solved = False
        error = "The cube is impossible to solve."

    return sequence, is_solved, error
