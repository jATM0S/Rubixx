from . import moves
from . import topCrossCases

def top_cross(rubiks_cube):
    sequence=[]
    moves.print_2d_cube(rubiks_cube)
    count=0
    for pos in ['U2', 'U4', 'U6','U8']:
        if rubiks_cube[pos] == rubiks_cube['U5'] :
            count+=1
    print(count)
    if count==4:
        return sequence,rubiks_cube
    if count==2:
        if all(rubiks_cube[pos]==rubiks_cube['U5'] for pos in ['U2','U8']) or all(rubiks_cube[pos]==rubiks_cube['U5'] for pos in ['U4','U6']):
            sequence=topCrossCases.line(rubiks_cube)
        else:
            sequence=topCrossCases.L(rubiks_cube)
    if count==0:
        sequence=topCrossCases.dot(rubiks_cube)
    for x in sequence:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
        # moves.print_2d_cube(rubiks_cube)
        
    return sequence,rubiks_cube



# print(top_cross(rubiks_cube))