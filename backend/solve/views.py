
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import moves
from . import bottomCross
from . import bottomCorners
from . import secondLayer
from . import topCross
from . import topCrossOrientation
from . import topCorners
from . import topCornersOrientation
from . import validate

def checkCube(rubiks_cube):
    # check for different center colors
    if len({rubiks_cube['F5'], rubiks_cube['L5'], rubiks_cube['R5'], rubiks_cube['B5'], rubiks_cube['U5'], rubiks_cube['D5']}) != 6:
        return False,("There are no 6 distinct center colors.")
        
    # check for the number of colors
    faces=['F','R','B','L','U','D']
    # getting colors and its dictionary for number of colored stickers
    colors={rubiks_cube['F5']:0,rubiks_cube['R5']:0,rubiks_cube['L5']:0,rubiks_cube['B5']:0,rubiks_cube['U5']:0,rubiks_cube['D5']:0}
    for face in faces:
        for x in range(1,10):
            if rubiks_cube[f'{face}{x}'] in colors:
                colors[rubiks_cube[f'{face}{x}']] += 1

    wrongColors = {color: count for color, count in colors.items() if count != 9}
            
    if wrongColors: return False, (f"The number of colors are not even for the following colors: "+", ".join(f"{color}: {count}" for color, count in wrongColors.items()) )
    
    # check availability of side pieces
    neededSidePieces={frozenset({rubiks_cube['F5'], rubiks_cube['L5']}),    
                      frozenset({rubiks_cube['F5'], rubiks_cube['R5']}),
                      frozenset({rubiks_cube['F5'], rubiks_cube['U5']}),  
                      frozenset({rubiks_cube['F5'], rubiks_cube['D5']}),    
                      frozenset({rubiks_cube['R5'], rubiks_cube['U5']}),    
                      frozenset({rubiks_cube['R5'], rubiks_cube['D5']}),    
                      frozenset({rubiks_cube['L5'], rubiks_cube['U5']}),    
                      frozenset({rubiks_cube['L5'], rubiks_cube['D5']}),
                      frozenset({rubiks_cube['B5'], rubiks_cube['L5']}),    
                      frozenset({rubiks_cube['B5'], rubiks_cube['R5']}),
                      frozenset({rubiks_cube['B5'], rubiks_cube['U5']}),  
                      frozenset({rubiks_cube['B5'], rubiks_cube['D5']})}

    sidePieces={frozenset({rubiks_cube['F4'], rubiks_cube['L6']}),
                frozenset({rubiks_cube['F6'], rubiks_cube['R4']}),
                frozenset({rubiks_cube['F2'], rubiks_cube['U8']}),
                frozenset({rubiks_cube['F8'], rubiks_cube['D2']}),  
                frozenset({rubiks_cube['B4'], rubiks_cube['R6']}), 
                frozenset({rubiks_cube['B6'], rubiks_cube['L4']}),
                frozenset({rubiks_cube['B2'], rubiks_cube['U2']}),
                frozenset({rubiks_cube['B8'], rubiks_cube['D8']}),
                frozenset({rubiks_cube['R2'], rubiks_cube['U6']}),
                frozenset({rubiks_cube['R8'], rubiks_cube['D6']}),    
                frozenset({rubiks_cube['L2'], rubiks_cube['U4']}),
                frozenset({rubiks_cube['L8'], rubiks_cube['D4']}),}
    if  sidePieces!=neededSidePieces:
        return False, ("The side pieces are incorrect.")


    # check availability of corner pieces
    neededCornerPieces={frozenset({rubiks_cube['F5'],rubiks_cube['L5'],rubiks_cube['U5']}),
                        frozenset({rubiks_cube['F5'],rubiks_cube['L5'],rubiks_cube['D5']}),
                        frozenset({rubiks_cube['F5'],rubiks_cube['R5'],rubiks_cube['U5']}),
                        frozenset({rubiks_cube['F5'],rubiks_cube['R5'],rubiks_cube['D5']}),
                        frozenset({rubiks_cube['B5'],rubiks_cube['L5'],rubiks_cube['U5']}),
                        frozenset({rubiks_cube['B5'],rubiks_cube['L5'],rubiks_cube['D5']}),
                        frozenset({rubiks_cube['B5'],rubiks_cube['R5'],rubiks_cube['U5']}),
                        frozenset({rubiks_cube['B5'],rubiks_cube['R5'],rubiks_cube['D5']}),}
    cornerPieces = {
    frozenset({rubiks_cube['F1'], rubiks_cube['L3'], rubiks_cube['U7']}),  # Front-Left-Up
    frozenset({rubiks_cube['F7'], rubiks_cube['L9'], rubiks_cube['D1']}),  # Front-Left-Down
    frozenset({rubiks_cube['F3'], rubiks_cube['R1'], rubiks_cube['U9']}),  # Front-Right-Up
    frozenset({rubiks_cube['F9'], rubiks_cube['R7'], rubiks_cube['D3']}),  # Front-Right-Down
    frozenset({rubiks_cube['B1'], rubiks_cube['R3'], rubiks_cube['U3']}),  # Back-Right-Up
    frozenset({rubiks_cube['B7'], rubiks_cube['R9'], rubiks_cube['D9']}),  # Back-Right-Down
    frozenset({rubiks_cube['B3'], rubiks_cube['L1'], rubiks_cube['U1']}),  # Back-Left-Up
    frozenset({rubiks_cube['B9'], rubiks_cube['L7'], rubiks_cube['D7']}),  # Back-Left-Down
    }
    if neededCornerPieces!=cornerPieces:
        return False, ("The corner piece is incorrect.")

    return True,""

def solve_cube(rubiks_cube):
    sequence=[]

    solvable,error=checkCube(rubiks_cube)
    if solvable==False:return [],False,error
    
    try:
        print("bottomcross")
        crossSequence,rubiks_cube=bottomCross.bottomCross(rubiks_cube)
        sequence.extend(crossSequence)
        print(crossSequence)
        solvable=validate.checkBottomCross(rubiks_cube)
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 1 failed, there is a problem with side of {rubiks_cube["D5"]} color.')

    try:
        print("bottomcorners")
        cornersSequence,rubiks_cube=bottomCorners.bottomCorners(rubiks_cube)
        sequence.extend(cornersSequence)
        print(cornersSequence)
        solvable=validate.checkBottomCorners(rubiks_cube)
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 2 failed, there is a problem with corner of {rubiks_cube["D5"]} color.')
        
    try:
        print("2nd layer")
        secondLayerSequence,rubiks_cube=secondLayer.secondLayer(rubiks_cube)
        sequence.extend(secondLayerSequence)
        print(secondLayerSequence)
        solvable=validate.checkSecondLayer(rubiks_cube)
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 3 failed, there is a problem with side of second layer.')
        
    try:
        print("topCross")
        topCrossSequence,rubiks_cube=topCross.top_cross(rubiks_cube)
        sequence.extend(topCrossSequence)
        print(topCrossSequence)
        solvable=validate.checkTopCross(rubiks_cube)
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 4 failed, there is a problem with side of {rubiks_cube["U5"]} color.')
        
    try:
        print("topcrossOrientation")
        topCrossOrientationSequence,rubiks_cube=topCrossOrientation.topCrossOrientation(rubiks_cube)
        sequence.extend(topCrossOrientationSequence)
        print(topCrossOrientationSequence)
        solvable=validate.checkTopCrossOrientation(rubiks_cube)
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 5 failed, there is a problem with side of {rubiks_cube["D5"]} color.')
        
    try:
        print("topCorners")
        topCornersSequence,rubiks_cube=topCorners.topCorners(rubiks_cube)
        sequence.extend(topCornersSequence)
        print(topCornersSequence)
        solvable=validate.checkTopCorners(rubiks_cube)
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 6 failed, there is a problem with corner of {rubiks_cube["U5"]} color.')
        
    try:
        print("topCornersOrientation")
        topCornersOrientationSequence,rubiks_cube=topCornersOrientation.topCornersOrienation(rubiks_cube)
        sequence.extend(topCornersOrientationSequence)
        print(topCornersOrientationSequence)
        solvable=validate.checkTopCornersOrietation(rubiks_cube)
    except Exception as e:
        solvable=False
    if solvable==False:return [],False,(f'Step 7 failed, there is a problem with corner of {rubiks_cube["U5"]} color.')
        
    moves.print_2d_cube(rubiks_cube)

    return sequence,True,""

@csrf_exempt
def solve_cube_view(request):
    if request.method == "GET":
        # Get the Rubik's Cube configuration from the query parameters or from the body
        data=json.loads(request.body)
        rubiks_cube = data.get('rubiks_cube')  

        # Solve the cube and get the sequence and solved status
        sequence, is_solved, error= solve_cube(rubiks_cube)

        # Return the result as a JSON response
        response = {
            'sequence': sequence,
            'is_solved': is_solved,
            'error':error
        }
        return JsonResponse(response)
# print(solve_cube(rubiks_cube))
# print(checkSolved(rubiks_cube))