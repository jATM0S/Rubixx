import random
from . import moves
def randomize(rubiks_cube):
    sequence=[]
    randomMoves=['f',"f'",'r',"r'",'l',"l'",'u',"u'",'d',"d'",'b',"b'",'rr','rl','ru','rd']
    noOfMoves=random.randint(25,50)
    for x in range(noOfMoves):
        sequence.append(random.choice(randomMoves))
    for x in sequence:
        rubiks_cube=moves.execute_move(rubiks_cube,x)
    
    return rubiks_cube
