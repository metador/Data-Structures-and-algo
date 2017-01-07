from __future__ import division


def game( num , is_player_turn,level ):
    if (num-1 < 1  or num/2 < 1): # check if in next step the game will end
        if  is_player_turn:    # check if it is the players turn
          # if the game ends in next step in both operations and its the selected players turn then he is cold
            if (num-1 < 1  and num/2 < 1):
                return False # it is cold for current player
            # if the subraction ends but not division and its the selected players turn he will chose division and contiue playing, avoiding the cold side
            elif num-1<1:
                return game(num/2, not is_player_turn,level+1)
            # if the division ends but not subtraction and its selected players turn then chose substration and continue playing Avoiding the cold side
            elif num/2<1:
                return game(num -1, not is_player_turn, level + 1)
        # if its the opposition players turn
        else:
            # if both operations end, then the opposition is cold. So selected player is hot
            if (num-1 < 1  and num/2 < 1):
                return True # it is hot for selected player
            #similary to selected player the opposition player avoid the hot side
            elif num-1<1:
                return game(num/2, not is_player_turn,level+1)
            elif num/2<1:
                return game(num -1, not is_player_turn, level + 1)


    # if the game is not about to end the recurse Till the end(base condition)
    left = game(num-1,not is_player_turn,level+1)
    right = game(num/2, not is_player_turn,level+1)

    if is_player_turn:
        # if it is the selected players turn, then the selected player will chose the hot side. In other words he will have the move which will make him hot
        if (right or left):
            return True
        # if there is no hot side for the selected player, he is cold
        elif not (right and left):
            return False
    # if it is the opposition players turn
    else:
        # if its hot on both operation for the selected player. Then no matter what the opposition player chooses, it will  be cold for selected player)
        if (right and left):
            return True
        #if it is cold on both operations for the selected player, then the opposition player can choose any operation and be cold for selected player
        elif not (right and left):
            return False
        #if there is one operation that is hot and another what is cold, then the oppostion player will chose the cold operation
        elif(right or left):
            return False

print game(7,True,1)