# Yang Tang 53979886
import connectfour

def display_board(GameState:connectfour.GameState):
    '''
    display the game board
    '''
    for i in range(connectfour.BOARD_COLUMNS):
        print(i+1,end='  ')
    print()
    for n in range(connectfour.BOARD_ROWS):
        for m in range(connectfour.BOARD_COLUMNS):
            if GameState.board[m][n]==connectfour.NONE:
                print('.',end='  ')
            elif GameState.board[m][n]==connectfour.RED:
                print('R',end='  ')
            elif GameState.board[m][n]==connectfour.YELLOW:
                print('Y',end='  ')
        print()

def dop_or_pop():
    '''
    choose the command
    '''
    print('drop or pop?')
    n=input()
    return n

def choose_drop(GameState:connectfour.GameState):
    '''
    handle the drop command, return gamestate and column number
    '''
    while True:
        n=choose_column()
        if 7>n-1>=0:
            try:
                GameState=connectfour.drop(GameState,n-1)
                display_board(GameState)
                return GameState,n
            except connectfour.InvalidMoveError:
                print('Invalid move')
            except connectfour.GameOverError:
                print('Game over')
        else:
            print('Invalid number, please enter 1 to 7')
            continue
        
def choose_pop(GameState:connectfour.GameState):
    '''
    handle the pop command, return gamestate and column number
    '''
    while True:
        n=choose_column()
        if 7>n-1>=0:
            GameState=connectfour.pop(GameState,n-1)
            display_board(GameState)
            return GameState,n
        else:
            print('Invalid number, please enter 1 to 7')
            continue
        
def check_winner(GameState:connectfour.GameState):
    '''
    check if there is a winner or not, return int
    '''
    n=connectfour.winner(GameState)
    return n
        
def choose_column():
    '''
    choose the column
    '''
    print('Which column?')
    while True:
        n=input()
        try:
            n=int(n)
            return n
        except:
            print('Invalid command, please enter 1 to 7')       

        
def welcome_banner():
    '''show the welcome banner'''
    print("WELCOME TO CONNECTFOUR!")
