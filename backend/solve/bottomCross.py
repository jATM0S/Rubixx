from . import bottomCrossCases
from . import moves

# cases and moves for each situation
def bring_piece_to_F8(rubiks_cube,side_pieces,moving_piece):
    if(moving_piece==side_pieces[0]):
        return bottomCrossCases.piece_on_front_top(rubiks_cube)
    elif(moving_piece==side_pieces[1]):
        return bottomCrossCases.piece_on_front_left(rubiks_cube)
    elif(moving_piece==side_pieces[2]):
        return bottomCrossCases.piece_on_front_right(rubiks_cube)
    elif(moving_piece==side_pieces[3]):
        return bottomCrossCases.piece_on_front_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[4]):
        return bottomCrossCases.piece_on_back_top(rubiks_cube)
    elif(moving_piece==side_pieces[5]):
        return bottomCrossCases.piece_on_left_top(rubiks_cube)
    elif(moving_piece==side_pieces[6]):
        return bottomCrossCases.piece_on_right_top(rubiks_cube)
    elif(moving_piece==side_pieces[7]):
        return bottomCrossCases.piece_on_right_right(rubiks_cube)
    elif(moving_piece==side_pieces[8]):
        return bottomCrossCases.piece_on_left_left(rubiks_cube)
    elif(moving_piece==side_pieces[9]):
        return bottomCrossCases.piece_on_back_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[10]):
        return bottomCrossCases.piece_on_right_bottom(rubiks_cube)
    elif(moving_piece==side_pieces[11]):
        return bottomCrossCases.piece_on_left_bottom(rubiks_cube)
    
# to dectect the white piece
def dectect_required_side_pieces(rubiks_cube,side_pieces):
    white_side_piece_positions=[]
    for pair in side_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['D5']:  # Check if the position has a white piece
                white_side_piece_positions.append(pair)    

    return white_side_piece_positions


# function to get the white and front center colored piece 
def frontCenter_piece_position(rubiks_cube,white_side_pieces):
    fc_colored_piece_position=[]
    for pair in white_side_pieces:
        for position in pair:  # Iterate over each position in the current pair
            if rubiks_cube[position] == rubiks_cube['F5']: 
                fc_colored_piece_position=pair
    return fc_colored_piece_position


def bottomCross(rubiks_cube):
    side_pieces=[['F2','U8'],['F4','L6'],['F6','R4'],['F8','D2'],['U2','B2'],['U4','L2'],['U6','R2'],['B4','R6'],['B6','L4'],['B8','D8'],['R8','D6'],['L8','D4']]
    sequence=[]
    moves.print_2d_cube(rubiks_cube)
    for i in range(4):
        if rubiks_cube['F8']==rubiks_cube['F5'] and rubiks_cube['R8']==rubiks_cube['R5'] and rubiks_cube['B8']==rubiks_cube['B5'] and rubiks_cube['L8']==rubiks_cube['L5'] and rubiks_cube['D2']==rubiks_cube['D5']and rubiks_cube['D4']==rubiks_cube['D5'] and rubiks_cube['D6']==rubiks_cube['D5'] and rubiks_cube['D8']==rubiks_cube['D5']:
            return sequence,rubiks_cube
        
        required_side_pieces=dectect_required_side_pieces(rubiks_cube,side_pieces)
        print(required_side_pieces)

        required_piece=frontCenter_piece_position(rubiks_cube,required_side_pieces)
        print(required_piece)
        
        face_moves=bring_piece_to_F8(rubiks_cube,side_pieces,required_piece)
        print(face_moves)
        for move in face_moves:
            print(move)
            rubiks_cube = moves.execute_move(rubiks_cube, move)
            moves.print_2d_cube(rubiks_cube) 
        
        print("next face")
        print('rl')
        rubiks_cube=moves.rotateLeft(rubiks_cube)
        moves.print_2d_cube(rubiks_cube)
        sequence.extend(face_moves)
        sequence.append('rl')


    return sequence,rubiks_cube

