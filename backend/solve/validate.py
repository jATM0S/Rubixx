from . import moves
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
