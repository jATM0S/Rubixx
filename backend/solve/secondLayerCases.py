def piece_on_front_top(rubiks_cube):
    sequence = []
    
    # Decide on the sequence of moves based on the condition
    if rubiks_cube['U8']==rubiks_cube['R5']:
        sequence=['u']        
        sequence.extend(['r','u',"r'","u'"])
        sequence.extend(["f'","u'",'f'])
    else:
        sequence=["u'"]
        sequence.extend(["l'","u'",'l',"u"])
        sequence.extend(['f','u',"f'","u'"])
    return sequence

def piece_on_frontLeft(rubiks_cube):
    sequence=[]
    sequence.extend(["l'","u'",'l',"u"])
    sequence.extend(['f','u',"f'"])
    return sequence
def piece_on_frontRight(rubiks_cube):
    sequence=[]        
    sequence.extend(['r','u',"r'","u'"])
    sequence.extend(["f'","u'",'f'])
    return sequence
def piece_on_rightRight(rubiks_cube):
    sequence=[]
    sequence.extend(['b','u',"b'","u'"])
    sequence.extend(["r'","u'",'r'])
    return sequence
def piece_on_leftLeft(rubiks_cube):
    sequence=[]
    sequence.extend(["b'","u'",'b','u'])
    sequence.extend(['l','u',"l'"])
    return sequence