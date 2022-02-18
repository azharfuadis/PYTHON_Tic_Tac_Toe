from random import randrange

def display_board(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[0][0]+'   |   '+board[0][1]+'   |   '+board[0][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[1][0]+'   |   '+board[1][1]+'   |   '+board[1][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '+board[2][0]+'   |   '+board[2][1]+'   |   '+board[2][2]+'   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    
def enter_move(board):
    
    while True:
        move = int(input("Please pick a number within the range of the squares (1-9): "))
        
        if move < 1 or move > 9:
            print("Please pick a number in range 1 to 9!")
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('Sorry that square is already taken, please take another one! ')
            continue
        
        for row in range(0,3):
            for column in range(0,3):
                if board[row][column]==str(move):
                    board[row][column]='O'
                
        break        

def make_list_of_free_fields(board):
    
    global free_fields
    free_fields = []
    
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column]=='X' or board[row][column]=='O':
                pass
            else:
                free_fields.append(([row],[column])) #appending tuple
    print(free_fields)
                
def victory_for(board, sign):
    
    if sign == "X":
        print('Checking to see if YOU are the winner...')
    else:
        print('Checking to see if the computer has won the game...')
    
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True
    else:
        print("We don\'t have a winner yet!")

def draw_move(board):
    
    while True:
        
        row = randrange(3)
        column = randrange(3)
        
        if ([row],[column]) not in free_fields:
            continue
        else:
            board[row][column] = 'X'
            return

board=[['1','2','3'],['4','X','6'],['7','8','9']]
number_of_moves =1 #board[1][1]="X"
human = 'O'
computer = 'X'

print('Hello and Welcome to Tic-Tac-Toe made in Python!')
print('\nHere is the current status of our game board: ')
display_board(board)
print()

while number_of_moves < 9:
# the following code covers the human's turn each round    
    enter_move(board)    
    number_of_moves += 1
    display_board(board)
    
    if victory_for(board, human) == True:
        print('You beat the computer, super!!!')
        break
    else:
        print('Here is the current list of the free fields, our board, and the status: ')
        make_list_of_free_fields(board)            
        print()
        display_board(board)    

# the following code covers the computer's turn each round            
    print()
    print('Now it\'s time for the computer to make its move!')
    draw_move(board)
    number_of_moves += 1
    display_board(board)
    print()
    
    if victory_for(board, computer) == True:
        print('You got outclassed by the computer')
        break
    else:
        print('Here is the current list of the free fields, our board, and the status: ')
        make_list_of_free_fields(board)            
        print()
        display_board(board)

else:
    print('We have a tie! This is a cat\'s game!!!')
    
print('Thanks for playing, see you in the next game!!!')
    
#computer starts first and finish last