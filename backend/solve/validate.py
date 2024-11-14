from . import moves

def checkBottomCross(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if rubiks_cube[F'{face}5']!=rubiks_cube[f'{face}8']:
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['2','4','6','8']):
        return False 
    return True
def checkBottomCorners(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all(rubiks_cube[F'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    return True

def checkSecondLayer(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all (rubiks_cube[F'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['4','6','7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    return True    

def checkTopCross(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all (rubiks_cube[F'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['4','6','7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    if not all (rubiks_cube['U5']==rubiks_cube[f'U{x}']for x in ['2','4','6','8']):
        return False
    return True    
def checkTopCrossOrientation(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all (rubiks_cube[F'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['2','4','6','7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    if not all (rubiks_cube['U5']==rubiks_cube[f'U{x}']for x in ['2','4','6','8']):
        return False    
    return True

def checkTopCorners(rubiks_cube):
    faces=['F','L','R','B']
    for face in faces:
        if not all (rubiks_cube[f'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['2','4','6','7','8','9']):
            return False
    if not all( rubiks_cube['D5']==rubiks_cube[f'D{x}'] for x in ['1','2','3','4','6','8','9']):
        return False 
    if not all (rubiks_cube['U5']==rubiks_cube[f'U{x}']for x in ['2','4','6','8']):
        return False
    for x in range(4):
        if {rubiks_cube['F5'],rubiks_cube['U5'],rubiks_cube['L5']}!={rubiks_cube['F1'],rubiks_cube['U7'],rubiks_cube['L3']}:
            return False
        rubiks_cube=moves.execute_move(rubiks_cube,'rl')
    return True
def checkTopCornersOrietation(rubiks_cube):
    faces=['F','L','R','B','U','D']
    for face in faces:
        if not all (rubiks_cube[f'{face}5']==rubiks_cube[f'{face}{x}'] for x in ['2','4','6','7','8','9']):
            return False
    return True
