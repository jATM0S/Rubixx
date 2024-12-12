from django.test import SimpleTestCase

from . import moves
from . import validate
from . import solve_cube
from . import randomize
from . import bottomCross
from . import bottomCorners
from . import secondLayer
from . import topCross
from . import topCrossOrientation
from . import topCorners
from . import topCornersOrientation


def solve_cube_test(rubiks_cube):
    sequence=[]

    solvable,error=validate.checkCube(rubiks_cube)
    if solvable==False:return [],False,error
    sequenceCube=rubiks_cube.copy()
    try:
        print("bottomcross")
        crossSequence,rubiks_cube=bottomCross.bottomCross(rubiks_cube)
        sequence.extend(crossSequence)
        print(crossSequence)
        solvable=validate.checkBottomCross(rubiks_cube)
        # for x in crossSequence:
        #     sequenceCube=moves.execute_move(sequenceCube,x)
        # if sequenceCube!=rubiks_cube:
        #     solvable=False
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 1 failed, there is a problem with side of {rubiks_cube["D5"]} color.')

    try:
        print("bottomcorners")
        cornersSequence,rubiks_cube=bottomCorners.bottomCorners(rubiks_cube)
        sequence.extend(cornersSequence)
        print(cornersSequence)
        solvable=validate.checkBottomCorners(rubiks_cube)
        # for x in cornersSequence:
        #     sequenceCube=moves.execute_move(sequenceCube,x)
        # if sequenceCube!=rubiks_cube:
        #     solvable=False
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 2 failed, there is a problem with corner of {rubiks_cube["D5"]} color.')
        
    try:
        print("2nd layer")
        secondLayerSequence,rubiks_cube=secondLayer.secondLayer(rubiks_cube)
        sequence.extend(secondLayerSequence)
        print(secondLayerSequence)
        solvable=validate.checkSecondLayer(rubiks_cube)
        # for x in secondLayerSequence:
        #     sequenceCube=moves.execute_move(sequenceCube,x)
        # if sequenceCube!=rubiks_cube:
        #     solvable=False
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 3 failed, there is a problem with side of second layer.')
        
    try:
        print("topCross")
        topCrossSequence,rubiks_cube=topCross.top_cross(rubiks_cube)
        sequence.extend(topCrossSequence)
        print(topCrossSequence)
        solvable=validate.checkTopCross(rubiks_cube)
        # for x in topCrossSequence:
        #     sequenceCube=moves.execute_move(sequenceCube,x)
        # if sequenceCube!=rubiks_cube:
        #     solvable=False
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 4 failed, there is a problem with side of {rubiks_cube["U5"]} color.')
        
    try:
        print("topcrossOrientation")
        topCrossOrientationSequence,rubiks_cube=topCrossOrientation.topCrossOrientation(rubiks_cube)
        sequence.extend(topCrossOrientationSequence)
        print(topCrossOrientationSequence)
        solvable=validate.checkTopCrossOrientation(rubiks_cube)
        # for x in topCrossOrientationSequence:
        #     sequenceCube=moves.execute_move(sequenceCube,x)
        # if sequenceCube!=rubiks_cube:
        #     solvable=False
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 5 failed, there is a problem with side of {rubiks_cube["D5"]} color.')
        
    try:
        print("topCorners")
        topCornersSequence,rubiks_cube=topCorners.topCorners(rubiks_cube)
        sequence.extend(topCornersSequence)
        print(topCornersSequence)
        solvable=validate.checkTopCorners(rubiks_cube)
        # for x in topCornersSequence:
        #     sequenceCube=moves.execute_move(sequenceCube,x)
        # if sequenceCube!=rubiks_cube:
        #     solvable=False
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 6 failed, there is a problem with corner of {rubiks_cube["U5"]} color.')
        
    try:
        print("topCornersOrientation")
        topCornersOrientationSequence,rubiks_cube=topCornersOrientation.topCornersOrienation(rubiks_cube)
        sequence.extend(topCornersOrientationSequence)
        print(topCornersOrientationSequence)
        solvable=validate.checkTopCornersOrietation(rubiks_cube)
        # for x in topCornersOrientationSequence:
        #     sequenceCube=moves.execute_move(sequenceCube,x)
        # if sequenceCube!=rubiks_cube:
        #     solvable=False
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 7 failed, there is a problem with corner of {rubiks_cube["U5"]} color.')
        
    moves.print_2d_cube(rubiks_cube)
    return sequence,True,""


def testValidation(cube):
    cubes=[]
    total=0
    noOftests=int(input("How many tests to run? "))
    for x in range (noOftests):
        try:
            rubiks_cube=randomize.randomize(cube)
            sequence,rubiks_cube=bottomCross.bottomCross(rubiks_cube)
            sequence,rubiks_cube=bottomCorners.bottomCorners(rubiks_cube)
            sequence,rubiks_cube=secondLayer.secondLayer(rubiks_cube)
            sequence,rubiks_cube=topCross.top_cross(rubiks_cube)
            sequence,rubiks_cube=topCrossOrientation.topCrossOrientation(rubiks_cube)
            sequence,rubiks_cube=topCorners.topCorners(rubiks_cube)
            sequence,rubiks_cube=topCornersOrientation.topCornersOrienation(rubiks_cube)
            solved=validate.checkTopCornersOrietation(rubiks_cube)
            if not solved:
                cubes.append(rubiks_cube)
            total+=len(sequence)
        except Exception as e:
            cubes.append(rubiks_cube)

    if not cubes:
        print("all test cases passed")
        return total/noOftests
    else:
        print("unsolved cubes")
        for x in cubes:
            moves.print_2d_cube(x)
        print(len(cubes))
        return cubes

class rubiks_test(SimpleTestCase):
    def setUp(self):
        self.rubiks_cube={'F1': 'O', 'F2': 'R', 'F3': 'O', 'F4': 'Y', 'F5': 'R', 'F6': 'O', 'F7': 'B', 'F8': 'Y', 'F9': 'Y', 'R1': 'G', 'R2': 'O', 'R3': 'B', 'R4': 'B', 'R5': 'G', 'R6': 'B', 'R7': 'G', 'R8': 'G', 'R9': 'W', 'B1': 'O', 'B2': 'Y', 'B3': 'W', 'B4': 'W', 'B5': 'O', 'B6': 'O', 'B7': 'R', 'B8': 'O', 'B9': 'O', 'L1': 'R', 'L2': 'R', 'L3': 'G', 'L4': 'W', 'L5': 'B', 'L6': 'G', 'L7': 'Y', 'L8': 'R', 'L9': 'R', 'U1': 'B', 'U2': 'B', 'U3': 'W', 'U4': 'W', 'U5': 'Y', 'U6': 'G', 'U7': 'Y', 'U8': 'B', 'U9': 'W', 'D1': 'Y', 'D2': 'R', 'D3': 'R', 'D4': 'G', 'D5': 'W', 'D6': 'W', 'D7': 'B', 'D8': 'Y', 'D9': 'G'}
    # def testOptimization(self):
    #     cubes=[]
    #     reason=[]
    #     totalOptimized=0
    #     totalUnoptimized=0
    #     # noOftests=int(input("How many tests to run? "))
    #     noOftests=5
    #     for x in range (noOftests):
    #         rubiks_cube=randomize.randomize(self.rubiks_cube)
    #         rub=rubiks_cube.copy()
    #         sequence,solved,error=solve_cube_test(rubiks_cube)
    #         if not solved:
    #             cubes.append(rub)
    #             reason.append(error)
    #         else:
    #             totalUnoptimized=totalUnoptimized+len(sequence)

    #             sequence=solve_cube.optimize(sequence)
    #             totalOptimized=totalOptimized+len(sequence)
    #             for x in sequence:
    #                 rubiks_cube=moves.execute_move(rubiks_cube,x)
                
    #             if validate.checkTopCornersOrietation(rubiks_cube)==False:
    #                 solved=False
    #                 reason.append('validation of optimization')
                
    #             if not solved:
    #                 cubes.append(rub)

    #     if not cubes:
    #         print(f"all {x} test cases passed")
    #         print(totalUnoptimized/noOftests,totalOptimized/noOftests)
    #         return 
    #     else:
    #         print(cubes,reason)
    #         return 
    def test(self):
        cubes=[]
        errors=[]
        total=0
        noOftests=5
        for x in range (noOftests):
            rubiks_cube=randomize.randomize(self.rubiks_cube)
            sequence,solved,error=solve_cube.solve_cube(self.rubiks_cube)
            if not solved:
                cubes.append(rubiks_cube)
                errors.append(error)
            total+=len(sequence)

        if not cubes:
            print(f"all {x} test cases passed")
            print(total/noOftests)
            return 
        else:
            print(cubes,errors)
            return 

# print(testValidation(rubiks_cube))
