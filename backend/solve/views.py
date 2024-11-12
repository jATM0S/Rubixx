
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
# rubiks_cube={'F1': 'G', 'F2': 'B', 'F3': 'O', 'F4': 'G', 'F5': 'Y', 'F6': 'G', 'F7': 'Y', 'F8': 'R', 'F9': 'B', 'R1': 'G', 'R2': 'O', 'R3': 'Y', 'R4': 'W', 'R5': 'B', 'R6': 'G', 'R7': 'R', 'R8': 'B', 'R9': 'W', 'B1': 'B', 'B2': 'W', 'B3': 'O', 'B4': 'Y', 'B5': 'W', 'B6': 'W', 'B7': 'R', 'B8': 'G', 'B9': 'B', 'L1': 'Y', 'L2': 'R', 'L3': 'R', 'L4': 'B', 'L5': 'G', 'L6': 'R', 'L7': 'W', 'L8': 'R', 'L9': 'O', 'U1': 'G', 'U2': 'O', 'U3': 'R', 'U4': 'Y', 'U5': 'R', 'U6': 'Y', 'U7': 'Y', 'U8': 'Y', 'U9': 'W', 'D1': 'B', 'D2': 'B', 'D3': 'W', 'D4': 'W', 'D5': 'O', 'D6': 'O', 'D7': 'O', 'D8': 'O', 'D9': 'G'}
def checkSolved(rubiks_cube):
    solved=False
    faces=['F','L','R','B','U','D']
    for face in faces:
        if not all(rubiks_cube[f'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['1','2','3','4','6','7','8','9']): 
            return False
    return True

def solve_cube(rubiks_cube):
    sequence=[]
    try:
        step=1
        print("bottomcross")
        crossSequence,rubiks_cube,solved=bottomCross.bottomCross(rubiks_cube)
        sequence.extend(crossSequence)
        print(crossSequence)

        step=2
        print("bottomcorners")
        cornersSequence,rubiks_cube,solved=bottomCorners.bottomCorners(rubiks_cube)
        sequence.extend(cornersSequence)
        print(cornersSequence)
        
        step=3
        print("2nd layer")
        secondLayerSequence,rubiks_cube=secondLayer.secondLayer(rubiks_cube)
        sequence.extend(secondLayerSequence)
        print(secondLayerSequence)
        
        step=4
        print("topCross")
        topCrossSequence,rubiks_cube=topCross.top_cross(rubiks_cube)
        sequence.extend(topCrossSequence)
        print(topCrossSequence)

        step=5
        print("topcrossOrientation")
        topCrossOrientationSequence,rubiks_cube=topCrossOrientation.topCrossOrientation(rubiks_cube)
        sequence.extend(topCrossOrientationSequence)
        print(topCrossOrientationSequence)

        step=6
        print("topCorners")
        topCornersSequence,rubiks_cube=topCorners.topCorners(rubiks_cube)
        sequence.extend(topCornersSequence)
        print(topCornersSequence)

        step=7
        print("topCornersOrientation")
        topCornersOrientationSequence,rubiks_cube=topCornersOrientation.topCornersOrienation(rubiks_cube)
        sequence.extend(topCornersOrientationSequence)
        print(topCornersOrientationSequence)
        
        moves.print_2d_cube(rubiks_cube)
        if checkSolved(rubiks_cube):
            return sequence,True
        else:
            return sequence,False
    except Exception as e:
            return sequence,False
        
    # return sequence
@csrf_exempt
def solve_cube_view(request):
    if request.method == "GET":
        # Get the Rubik's Cube configuration from the query parameters or from the body
        data=json.loads(request.body)
        rubiks_cube = data.get('rubiks_cube')  

        # Solve the cube and get the sequence and solved status
        sequence, is_solved = solve_cube(rubiks_cube)

        # Return the result as a JSON response
        response = {
            'sequence': sequence,
            'is_solved': is_solved
        }
        return JsonResponse(response)
# print(solve_cube(rubiks_cube))
# print(checkSolved(rubiks_cube))