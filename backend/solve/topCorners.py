from . import moves

def checkTopCorners(rubiks_cube):
    print("checkTopCorners")
    checkCorrect=False
    for x in range(4):
        if {rubiks_cube['F5'], rubiks_cube['U5'], rubiks_cube['L5']} <= {rubiks_cube['F1'], rubiks_cube['U7'], rubiks_cube['L3']}:
            rubiks_cube=moves.execute_move(rubiks_cube,'rl')
            checkCorrect=True
        else:
            checkCorrect=False
            return checkCorrect
    return checkCorrect


def findRequiredCorner(rubiks_cube):
    print("findRequiredCorner")
    sequence=[]
    requiredCornerExists=False
    moves.print_2d_cube(rubiks_cube)
    for x in range(4):
        if {rubiks_cube['F5'], rubiks_cube['U5'], rubiks_cube['L5']} <= {rubiks_cube['F1'], rubiks_cube['U7'], rubiks_cube['L3']}:
            requiredCornerExists=True
            if x ==0:
                sequence=[]
            elif x==1:
                sequence=['rl']
            elif x==2:
                sequence=['rl','rl']
            elif x==3:
                sequence=['rr']
            break
        else:
            rubiks_cube=moves.execute_move(rubiks_cube,'rl')
    return requiredCornerExists,sequence


def rightOrLeftNiklas(rubiks_cube):
    print("rightorLeftNIklas")
    sequence=[]
    if {rubiks_cube['F5'], rubiks_cube['R5'], rubiks_cube['U5']} <= {rubiks_cube['U1'], rubiks_cube['B3'], rubiks_cube['L1']}:
        sequence=['r',"u'","l'",'u',"r'","u'",'l','u']
    else:
        sequence=['rr',"l'",'u','r',"u'",'l','u',"r'","u'"]
    return sequence


def topCorners(rubiks_cube):
    sequence=[]
    # if oriented correctly returns as it is
    if checkTopCorners(rubiks_cube):
        return sequence,rubiks_cube
    # find the correct corner if it exists

    requiredCornerExists,cornerToFSequence=findRequiredCorner(rubiks_cube)
    if requiredCornerExists:
        print(cornerToFSequence)
        for x in cornerToFSequence:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
        sequence.extend(cornerToFSequence)
    
    # if correct corner does not exits then do a sune and go to the corrected corner
    else:
        print('making one correct corner')
        sequence.extend(['r',"u'","l'",'u',"r'","u'",'l','u'])
        for x in sequence:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
        requiredCornerExists,cornerToFSequence=findRequiredCorner(rubiks_cube)
        print(cornerToFSequence)
        for x in cornerToFSequence:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
        sequence.extend(cornerToFSequence)
        
    
    # if left side move is to be done or right side move is to be done decide
    niklas=rightOrLeftNiklas(rubiks_cube)        
    print(niklas)
    for x in niklas:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
        moves.print_2d_cube(rubiks_cube)
    sequence.extend(niklas)
    
    return sequence,rubiks_cube


# moves.print_2d_cube(rubiks_cube)
# print(topCorners(rubiks_cube))