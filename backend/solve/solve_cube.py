from . import moves
from . import bottomCross
from . import bottomCorners
from . import secondLayer
from . import topCross
from . import topCrossOrientation
from . import topCorners
from . import topCornersOrientation
from . import validate

def optimize(sequence):
    x=0
    while x in range(len(sequence)):
        first=sequence[x]
        if x+1<len(sequence):
            second=sequence[x+1]
        else: second=None
        if x+2<len(sequence):
            third=sequence[x+2]
        else:third=None
        if x+3<len(sequence):
            fourth=sequence[x+3]
        else: fourth=None

        e4=False
        if fourth: 
            if first==second==third==fourth:
                print(f"remove 4 repeat at index {x}")
                print(first,second,third,fourth)
                print(sequence)
                del sequence[x:x+4]
                print(sequence)
                x-=1
                e4=True

        e3=False
        if not e4 and third:
            if first==second==third:
                print(f"remove 3 repeat at index {x}")
                print(first,second,third)
                print(sequence)
                if first.endswith("'"):
                    sequence[x:x+3]=first[:-1]
                else:
                    if first=='rl':
                        sequence[x:x+3]=['rr']
                    elif first=='rr':
                        sequence[x:x+3]=['rl']
                    else:
                        sequence[x:x+3]=[first+"'"]
                print(sequence)
                e3=True
                x-=1
        
        if not e3 and not e4 and second:
            if first+"'"==second or first==second+"'" or (first=='rl' and second=='rr') or (first=='rr' and second=='rl'):
                print(f"remove two opossite at index {x}")
                print(first,second)
                print(sequence)
                del sequence[x:x+2]
                print(sequence)
                x-=1

        x+=1
    return sequence

def solve_cube(rubiks_cube):
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
    sequence=optimize(sequence)
    for x in sequence:
        sequenceCube=moves.execute_move(sequenceCube,x)
    if sequenceCube!=rubiks_cube:
        return [],False,"sequence error"
    return sequence,True,""