board = {'7': '', '8': '', '9': '',
         '4': '', '5': '', '6': '',
         '1': '', '2': '', '3': ''}

board_keys = []

for  key in board:
    board_keys.append(key)

    '''We will define the printBoard function in order to print the board everytime
    by calling this function.'''

def printBoard(game_board):
    print(game_board['7'] + '|' + game_board['8'] + '|' + game_board['9'])
    print('-+-+-')
    print(game_board['4'] + '|' + game_board['5'] + '|' + game_board['6'])
    print('-+-+-')
    print(game_board['1'] + '|' + game_board['2'] + '|' + game_board['3'])
# this function define the game
def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(board)
        print("It's your turn," + turn + "Where to go?")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else: 
            print("This place is already filled. \nWhere to go?")
            continue
#We will check if player X or O has won in 5 moves.

if count >= 5:
    if board['7'] == board['8'] == board['9'] != ' ':
        printBoard(board)
        print('\nGame over.\n')
        print (turn + "won.")
        break
    elif board['4'] == board['5'] == board['6'] != ' ':
        printBoard(board)
        print('\nGame over.\n')
        print (turn + "won.")
        break
    elif board['1'] == board['2'] == board['3'] != ' ':
        printBoard(board)
        print('\nGame over.\n')
        print (turn + "won.")
        break
    elif board['2'] == board['5'] == board['8'] != ' ':
        printBoard(board)
        print('\nGame over.\n')
        print (turn + "won.")
        break
    elif board['3'] == board['6'] == board['9'] != ' ':
        printBoard(board)
        print('\nGame over.\n')
        print (turn + "won.")
        break
    elif board['1'] == board['4'] == board['7'] != ' ':
        printBoard(board)
        print('\nGame over.\n')
        print (turn + "won.")
        break
    elif board['7'] == board['5'] == board['3'] != ' ':#diagonal
        printBoard(board)
        print('\nGame over.\n')
        print (turn + "won.")
        break
    elif board['9'] == board['5'] == board['1'] != ' ': #diagonal
        printBoard(board)
        print('\nGame over.\n')
        print (turn + "won.")
        break

    #in case of 'tie'

    if count == 9:
        print("\nIt's a Tie!")

    #Change the player after every move.

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'