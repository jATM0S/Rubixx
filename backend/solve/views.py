from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cube(request):
    rubiks_cube = {
    'F1': 'green', 'F2': 'green', 'F3': 'green', 'F4': 'green', 'F5': 'green', 'F6': 'green', 'F7': 'green', 'F8': 'green', 'F9': 'green',
    'B1': 'blue', 'B2': 'blue', 'B3': 'blue', 'B4': 'blue', 'B5': 'blue', 'B6': 'blue', 'B7': 'blue', 'B8': 'blue', 'B9': 'blue',
    'L1': 'orange', 'L2': 'orange', 'L3': 'orange', 'L4': 'orange', 'L5': 'orange', 'L6': 'orange', 'L7': 'orange', 'L8': 'orange', 'L9': 'orange',
    'R1': 'red', 'R2': 'red', 'R3': 'red', 'R4': 'red', 'R5': 'red', 'R6': 'red', 'R7': 'red', 'R8': 'red', 'R9': 'red',
    'U1': 'white', 'U2': 'white', 'U3': 'white', 'U4': 'white', 'U5': 'white', 'U6': 'white', 'U7': 'white', 'U8': 'white', 'U9': 'white',
    'D1': 'yellow', 'D2': 'yellow', 'D3': 'yellow', 'D4': 'yellow', 'D5': 'yellow', 'D6': 'yellow', 'D7': 'yellow', 'D8': 'yellow', 'D9': 'yellow'
    }
    return HttpResponse("Hello, this is the solve view!")
