import random
from time import sleep
board_current = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']] #starting list that represents a blank board that's global
end_game = someone_won = False #set the game to not over and that nobody has won yet
def display_board(board):
    sleep(1)
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] + '   |   ' + board [0][1] + '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] + '   |   ' + board [1][1] + '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] + '   |   ' + board [2][1] + '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

# The function browses the board and builds a list of all the free square numbers;
def make_list_of_free_squares(board):
    lst_free_squares = []
    for row in board:
        for square in row:
            if square != 'O' and square != 'X':
                lst_free_squares.append(int(square))
    return (lst_free_squares)

# The function accepts the board's current status, asks the user about their move,
# checks the input, and updates the board according to the user's decision:
def player_enter_move(board):
    move_acceptable = False #Dummy variable to keep looping until either a good move is made or the player stops the game
    sleep(2)
    move = input('Enter the square you would like to take, or -1 to end the game: ')
    while move_acceptable == False:
        try:
            move = int(move)
        except:
            sleep(2)
            move = input('Enter the number of the square that you would like to take, or -1 to end the game: ')
            continue #back to while loop
        if move == -1:
            sleep(1)
            print('You\'ve ended the game.')
            sleep(2)
            print('Good-bye')
            sleep(2)
            global end_game
            end_game = True
            break
        elif (move < 1) or (move > 9):
            sleep(1)
            print('OK, maybe you don\'t have your glasses on.')
            sleep(2)
            move = input('Please enter a square number between 1 and 9, or -1 to end the game: ')
            continue
        elif move not in make_list_of_free_squares(board):
            sleep(1)
            print('Yes, it would be nice to be able to choose that square.')
            sleep(2)
            move = input('However, that square is already chosen. Please enter another, or -1 to end the game: ')
            continue #back to while loop
        else: #if a good move is indeed made:
            board[(move-1)//3][(move - 1) % 3] = 'O'
            move_acceptable = True

# This function draws the computer's move and updates the board.
#It is more efficient to choose randomly from available fields than to randomly choosing from the board
#and then filtering to see if it was an available move:
def computer_enter_move(board):
    x = make_list_of_free_squares(board)
    computer_move = random.choice(x)
    board[(computer_move-1)//3][(computer_move - 1) % 3] = 'X'
    sleep(2)
    print('Alright, the computer is choosing its move...')
    sleep(2)
    print('Ok, the computer has chosen its move.')

# The function analyzes the board's status in order to check if
# the player using 'O's or 'X's has won the game:
def victory_for(board, sign):
    global someone_won #in case a victory occurs, this will be recognized outside of this function
    if sign == 'O':
        vertically = horizontally = diagonally = 0 #set variables about method of winning to zero for now
        #see if any methods of victory have been achieved by the player:
        if (board[0][0] == board[1][0] == board[2][0] == sign) or (board[0][1] == board[1][1] == board[2][1] == sign) or (board[0][2] == board[1][2] == board[2][2] == sign):
            vertically = 1
        if (board[0][0] == board[0][1] == board[0][2] == sign) or (board[1][0] == board[1][1] == board[1][2] == sign) or (board[2][0] == board[2][1] == board[2][2] == sign):
            horizontally = 1
        if (board[0][0] == board[1][1] == board[2][2] == sign) or (board[2][0] == board[1][1] == board[0][2] == sign):
            diagonally = 1

        #if exactly one victory method is achieved:
        if vertically + horizontally + diagonally == 1:
            statement = 'You win '
            if vertically == 1:
                statement = statement + 'vertically'
            if horizontally == 1:
                statement = statement + 'horizontally'
            if diagonally == 1:
                statement = statement + 'diagonally'
            sleep(2)
            print('Congratulations!')
            sleep(2)
            print(statement + '.')

        #if more than one victory method is achieved:
        if vertically + horizontally + diagonally > 1:
            statement = 'You win'
            if vertically == 1:
                statement = statement + ' vertically'
                if horizontally == 1:
                    statement = statement + ' and horizontally'
                if diagonally == 1:
                    statement = statement + ' and diagonally'
            elif horizontally == 1:
                statement = statement + ' horizontally'
                if diagonally == 1:
                    statement = statement + ' and diagonally'
            sleep(2)
            print('Congratulations!')
            sleep(2)
            print(statement + '.')

        #set win to be True so it the program afterwards can proceed accordingly:
        if vertically + horizontally + diagonally > 0:
            someone_won = True

    if sign == 'X':
        vertically = horizontally = diagonally = 0 #set variables about method of winning to zero for now
        #see if any methods of victory have been achieved by the computer:
        if (board[0][0] == board[1][0] == board[2][0] == sign) or (board[0][1] == board[1][1] == board[2][1] == sign) or (board[0][2] == board[1][2] == board[2][2] == sign):
            vertically = 1
        if (board[0][0] == board[0][1] == board[0][2] == sign) or (board[1][0] == board[1][1] == board[1][2] == sign) or (board[2][0] == board[2][1] == board[2][2] == sign):
            horizontally = 1
        if (board[0][0] == board[1][1] == board[2][2] == sign) or (board[2][0] == board[1][1] == board[0][2] == sign):
            diagonally = 1

        #if exactly one method of victory is achieved by the computer:
        if vertically + horizontally + diagonally > 0 and vertically + horizontally + diagonally < 2:
            statement = 'The computer wins'
            if vertically == 1:
                statement = statement + ' vertically'
            if horizontally == 1:
                statement = statement + ' horizontally'
            if diagonally == 1:
                statement = statement + ' diagonally'
            sleep(2)
            print('Bummer, dude.')
            sleep(2)
            print(statement + '.')

        #if more than one method of victory is achieved by the computer:
        if vertically + horizontally + diagonally > 1:
            statement = 'The computer wins'
            if vertically == 1:
                statement = statement + ' vertically'
                if horizontally == 1:
                    statement = statement + ' and horizontally'
                if diagonally == 1:
                    statement = statement + ' and diagonally'
            elif horizontally == 1:
                statement = statement + ' horizontally'
                if diagonally == 1:
                    statement = statement + ' and diagonally'
            sleep(2)
            print('Bummer, dude.')
            sleep(2)
            print(statement + '.')

        #set win to be True so it the program afterwards can proceed accordingly:
        if vertically + horizontally + diagonally > 0:
            someone_won = True

#Here is the game in action:
print('\n' + 'Welcome to Tic-Tac-Toe!')
sleep(2)
print('Here is the current board: ')
display_board(board_current) #Display the board
while end_game == False:
    player_enter_move(board_current) # Player enters a move
    sleep(2)
    print('Here is how the board looks after your move: ')
    sleep(2)
    display_board(board_current)
    victory_for(board_current, 'O') # Check for player victory

    #If player did win:
    if someone_won == True:
        sleep(2)
        again = input('Would you like to play again? Enter yes or y to play again, or anything else to quit: ').lower()
        if again == 'yes' or again == 'y':
            sleep(2)
            print('OK, another round is coming up!')
            sleep(2)
            board_current = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print('\n' + '\n' + '\n')
            someone_won = end_game=  False
            sleep(2)
            print('Here is the current board: ')
            display_board(board_current) #Display the board
            continue #Get back to the while loop
        else:
            sleep(2)
            print('Good game! Thanks for playing.')
            sleep(1)
            quit()

    if len(make_list_of_free_squares(board_current)) == 0: # If there is no winner and there are no more available spots
        sleep(2)
        print('This game is a tie')
        sleep(2)
        again = input('Would you like to play again? Enter yes or y to play again, or anything else to quit: ').lower()
        if again == 'yes' or again == 'y':
            sleep(2)
            print('OK, another round is coming up!')
            sleep(2)
            board_current = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print('\n' + '\n' + '\n')
            someone_won = end_game=  False
            sleep(2)
            print('Here is the current board: ')
            display_board(board_current) #Display the board
            continue #Get back to the while loop
        else:
            sleep(2)
            print('Good game! Thanks for playing.')
            sleep(1)
            quit()
    if end_game == True:
        continue #skip over computer move to get to while loop if the game had ended
    computer_enter_move(board_current) # Computer enters a move
    sleep(2)
    print('Here is the current board: ')
    display_board(board_current)
    victory_for(board_current, 'X') # Check for computer victory

    #If computer did win:
    if someone_won == True:
        sleep(2)
        again = input('Would you like to play again? Enter yes or y to play again, or anything else to quit: ').lower()
        if again == 'yes' or again == 'y':
            sleep(2)
            print('OK, another round is coming up!')
            sleep(2)
            board_current = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            print('\n' + '\n' + '\n')
            someone_won = end_game=  False
            sleep(2)
            print('Here is the current board: ')
            display_board(board_current) #Display the board
            continue #Get back to the while loop
        else:
            sleep(2)
            print('Good game! Thanks for playing.')
            sleep(1)
            quit()
