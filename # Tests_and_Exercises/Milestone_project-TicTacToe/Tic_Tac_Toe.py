
#? =============================================================================
#* Milestone project - Tic Tac Toe
#? =============================================================================
import msvcrt #* Microsoft Visual C runtime Library
import os
import random
import time

#* Starting BOARD (empty)
play_board = [" "," "," "," "," "," "," "," "," "]

#* Clear the Console
def clear ():
    os.system("cls") 

#* Randomizer
def rand_2(player1, player2):
    return random.choice([player1, player2])

#* Display Board function
def display_board(board = [" "," "," "," "," "," "," "," "," "]):
    clear()
    print("<<< TIC TAC TOE GAME >>>\n")
    print("     =============")
    print(f"     | {board[6]} | {board[7]} | {board[8]} |")
    print("     =============")
    print(f"     | {board[3]} | {board[4]} | {board[5]} |")
    print("     =============")
    print(f"     | {board[0]} | {board[1]} | {board[2]} |")
    print("     =============\n")

#* Player input function
def player_input (player):
    print(f"{player} turn!")
    print("Please choose a field: ")
    input = True
    numlist = ["1","2","3","4","5","6","7","8","9"]
    while input:
        marker = msvcrt.getch()
        marker = str(marker, "utf-8")
        if marker in numlist:
            marker = int(marker)-1
            input = False
        else:
            print("Use numbers 1-9 to play!")
    return marker
    
#* Placing the marker
def mark (board,marker,sign,player):
    position_is_empty = (space_check(board,marker))
    while position_is_empty == False:
        print("This LOCATION is OCCUPIED! Choose another one!", end="\r")
        marker = player_input(player)
        position_is_empty = (space_check(board,marker))
    else:
        board[marker] = sign
        return board

#* Check win condition (3 in line)
def win_condition(board):
    
    if (
        board[0] == board[3] == board[6] == "X" or
        board[6] == board[7] == board[8] == "X" or
        board[2] == board[4] == board[6] == "X" or
        board[3] == board[4] == board[5] == "X" or
        board[0] == board[1] == board[2] == "X" or
        board[0] == board[4] == board[8] == "X" or
        board[1] == board[4] == board[7] == "X" or
        board[2] == board[5] == board[8] == "X"
    ):
        print("\nX is the winner!\n")
        return True
    elif(
        board[0] == board[3] == board[6] == "O" or
        board[6] == board[7] == board[8] == "O" or
        board[2] == board[4] == board[6] == "O" or
        board[3] == board[4] == board[5] == "O" or
        board[0] == board[1] == board[2] == "O" or
        board[0] == board[4] == board[8] == "O" or
        board[1] == board[4] == board[7] == "O" or 
        board[2] == board[5] == board[8] == "O"
    ):
        print("\nO is the winner!\n")
        return True
    else:
        return False
        
#* Space check - is the space available
def space_check(board, marker):
    if board[marker] == "X" or board[marker] == "O":
        return False
    else:
        return True
    
#* Full board - check if the board is full or not
def full_board(board):
    for element in board:
        if element == " ":
            return False
    return True
        
#* EXTRA: Waiting indicator
def waiting_indicator(duration):
    end_time = time.time() + duration
    symbols = ['\\', '|', '/', '-']
    index = 0
    while time.time() < end_time:
        print(symbols[index % len(symbols)], end='\r')
        index += 1
        time.sleep(0.1)


#* Test Board
numeric_board = [0,1,2,3,4,5,6,7,8]
test_board = ["X"," ","O","X","O","X","X","O","X"]

# ==============================================================================
#* GAME STARTS
# ==============================================================================

clear()
print("<<< TIC TAC TOE GAME >>>\n")
display_board(play_board)
time.sleep(2)
clear()

game_running = True
while game_running:
    # #*PLAYER 1 name
    # First_input = input("Player 1 ENTER Name: ")
    # print(f"Hello {First_input} !")
    # p1_sign = random.choice(["X", "O"])
    # time.sleep(3)
    # clear()

    # #*PLAYER 2 name
    # Second_input = input("Player 2 ENTER Name: ")
    # print(f"Hello {Second_input} !")
    # p2_sign = "O" if (p1_sign == "X") else "X"
    # time.sleep(3)
    # clear()
    
    # #*WHO WILL START:
    # print("Who will start? ...")
    # waiting_indicator(3)
    # clear()
    
    # player1 = rand_2(First_input, Second_input)
    # player2 = Second_input if player1 == First_input else First_input
    
    player1 = "Player 1"
    player2 = "Player 2"
    p1_sign = "X"
    p2_sign = "O"
        
    print(f"{player1} FIRST!!! Good Luck!")
    print(f"\n{player1} is |{p1_sign}|\n{player2} is |{p2_sign}|")
    time.sleep(3)
    clear()
    
    #*DISPLAY FIRST BOARD
    display_board(play_board)
    
    full = False
    winner = False
    
    while full == False and winner == False:
        #* PLAYER 1
        mark_p1 = player_input(player1)
        play_board = mark(play_board, mark_p1, p1_sign, player1)
        display_board(play_board)
        
        full = full_board(play_board)
        winner1 = win_condition(play_board)
        #* Check Win condition
        if full == True and winner1 == True:
            print(f"Congrats {player1}")
            break
        
        elif winner1 == True:
            print(f"Congrats {player1}\n")
            break
        
        elif full == True:
            print("\nDraw!\n")
            break
                
        #* PLAYER 2 TURN
        mark_p2 = player_input(player2)
        play_board = mark(play_board, mark_p2, p2_sign, player2)
        display_board(play_board)
        
        full = full_board(play_board)
        winner2 = win_condition(play_board)
        #* Check Win condition
        if full == True and winner2 == True:
            print(f"Congrats {player2}")
            break
        
        elif winner2 == True:
            print(f"Congrats {player2}\n")
            break
        
        elif full == True:
            print("\nDraw!\n")
            break        

    
    
    game_running = False