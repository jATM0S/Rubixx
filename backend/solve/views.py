
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import solve_cube
from . import randomize
from . import moves
@csrf_exempt
def solve_cube_view(request):
    if request.method == "GET":
        # Get the Rubik's Cube configuration from the query parameters or from the body
        data=json.loads(request.body)
        rubiks_cube = data.get('rubiks_cube')  

        # Solve the cube and get the sequence and solved status
        sequence, is_solved, error= solve_cube.solve_cube(rubiks_cube)

        # Return the result as a JSON response
        response = {
            'sequence': sequence,
            'is_solved': is_solved,
            'error':error
        }
        return JsonResponse(response)
@csrf_exempt
def scramble_cube_view(request):
    if request.method=="GET":
        # Get the Rubik's Cube configuration from the query parameters or from the body
        data=json.loads(request.body)
        rubiks_cube = data.get('rubiks_cube')  

        # do random moves on cube and get the scrambled
        rubiks_cube= randomize.randomize(rubiks_cube)

        # Return the result as a JSON response
        response = {
            'rubiks_cube': rubiks_cube,
        }
        return JsonResponse(response)
@csrf_exempt
def execute_move_view(request):
    if request.method=="GET":
        # Get the Rubik's Cube configuration from the query parameters or from the body
        data=json.loads(request.body)
        rubiks_cube = data.get('rubiks_cube')  
        move=data.get('move')
        # do random moves on cube and get the scrambled
        rubiks_cube= moves.execute_move(rubiks_cube,f'{move}')

        # Return the result as a JSON response
        response = {
            'rubiks_cube': rubiks_cube,
        }
        return JsonResponse(response)