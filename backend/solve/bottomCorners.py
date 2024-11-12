from . import bottomCornerCases
from . import moves

def bring_piece_to_F7(rubiks_cube,corner_pieces,moving_piece):
    if(moving_piece==corner_pieces[0]):
        return bottomCornerCases.front_top_left(rubiks_cube)
    elif(moving_piece==corner_pieces[1]):
        return bottomCornerCases.front_top_right(rubiks_cube)
    elif(moving_piece==corner_pieces[2]):
        return bottomCornerCases.front_bottom_left(rubiks_cube)
    elif(moving_piece==corner_pieces[3]):
        return bottomCornerCases.front_bottom_right(rubiks_cube)
    elif(moving_piece==corner_pieces[4]):
        return bottomCornerCases.left_left_top(rubiks_cube)
    elif(moving_piece==corner_pieces[5]):
        return bottomCornerCases.right_right_top(rubiks_cube)
    elif(moving_piece==corner_pieces[6]):
        return bottomCornerCases.left_left_bottom(rubiks_cube)
    elif(moving_piece==corner_pieces[7]):
        return bottomCornerCases.right_right_bottom(rubiks_cube)
    
        
# to dectect the white piece
def dectect_required_corner_pieces(rubiks_cube,corner_pieces):

    required_corner_pieces=[]
    for pair in corner_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['D5']:  # Check if the position has a white piece
                required_corner_pieces.append(pair)    

    return required_corner_pieces


# function to get the white and front center colored piece 
def leftCorner_piece_position(rubiks_cube,required_corner_pieces):
    leftCorner_piece_position=[]
    required_pieces=[]
    for pair in required_corner_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['F5']: 
                required_pieces.append(pair)
            
    for piece in required_pieces:
        for face in piece:
            if rubiks_cube[face]==rubiks_cube['L5']:
                leftCorner_piece_position=piece
    return leftCorner_piece_position

# def rightCorner_piece_position(rubiks_cube,white_corner_pieces):
#     rightCorner_piece_position=[]
#     required_pieces=[]
#     for pair in white_corner_pieces:
#         for position in pair:  # Iterate over each position in the current pair
#             if rubiks_cube[position] == rubiks_cube['F5']: 
#                 required_pieces.append(pair)
#     print(required_pieces)
#     for piece in required_pieces:
#         for face in piece:
#             if rubiks_cube[face]==rubiks_cube['R5']:
#                 rightCorner_piece_position=piece
#     return rightCorner_piece_position

def bottomCorners(rubiks_cube):
    corner_pieces=[['F1','U7','L3'],['F3','U9','R1'],['F7','L9','D1'],['F9','R7','D3'],['U1','L1','B3'],['U3','R3','B1'],['L7','D7','B9'],['R9','D9','B7']]
    sequence=[]
    moves.print_2d_cube(rubiks_cube)
    for x in range(4):
        if rubiks_cube['L9']==rubiks_cube['L5'] and rubiks_cube['F7']==rubiks_cube['F5'] and rubiks_cube['D1']==rubiks_cube['D5'] and rubiks_cube['F9']==rubiks_cube['F5'] and rubiks_cube['R7']==rubiks_cube['R5'] and rubiks_cube['D3']==rubiks_cube['D5'] and rubiks_cube['R9']==rubiks_cube['R5'] and rubiks_cube['B7']==rubiks_cube['B5'] and rubiks_cube['D9']==rubiks_cube['D5'] and rubiks_cube['L7']==rubiks_cube['L5'] and rubiks_cube['B9']==rubiks_cube['B5'] and rubiks_cube['D7']==rubiks_cube['D5']:
            return sequence, rubiks_cube
        
        required_corner_pieces=dectect_required_corner_pieces(rubiks_cube,corner_pieces)
        print(required_corner_pieces)
        leftCorner_piece=leftCorner_piece_position(rubiks_cube,required_corner_pieces)
        print(leftCorner_piece)

        face_moves=bring_piece_to_F7(rubiks_cube,corner_pieces,leftCorner_piece)
        print(face_moves)
        for x in face_moves:
            rubiks_cube=moves.execute_move(rubiks_cube,x)
            moves.print_2d_cube(rubiks_cube)
        sequence.extend(face_moves)
        rubiks_cube=moves.rotateLeft(rubiks_cube)
        moves.print_2d_cube(rubiks_cube)
        sequence.append('rl')
    return sequence,rubiks_cube


# print(bottomCorners(rubiks_cube))