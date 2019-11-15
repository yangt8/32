# Yang Tang 53979886
import I32CFSP
import connectfour
import connectfour_common

#HOST = 'woodhouse.ics.uci.edu'
#PORT = 4444

def _run_user_interface() -> None:
    '''
    user interface of the game
    '''
    HOST=str(input('HOST: '))
    PORT=int(input('PORT: '))
    connectfour_common.welcome_banner()
    connection = I32CFSP.connect(HOST, PORT)
    try:
        username = _ask_for_username()
        I32CFSP.hello(connection, username)
        I32CFSP.start_game(connection, username)
        main(connection)
    finally:
        I32CFSP.close(connection)
        
        
def main(connection: I32CFSP.ConnectfourConnection):
    '''
    main function of the game
    '''
    gamestate=connectfour.new_game()
    while True:
        message = I32CFSP._read_line(connection).upper()
        if message=='READY':
            print('Your turn')
            gamestate=choose_state(gamestate,connection)
        elif message=='OKAY':
            print("AI's turn")
            gamestate=ai(gamestate,connection)
        elif message=='INVALID':
            pass
        elif message == 'WINNER_YELLOW':
            if connectfour_common.check_winner(gamestate)==connectfour.YELLOW:
                print('YELLOW WINS')
                print('GAME OVER')
                break
        elif message == 'WINNER_RED':
            if connectfour_common.check_winner(gamestate)==connectfour.RED:
                print('RED WINS')
                print('GAME OVER')
                break
                

def ai(GameState:connectfour.GameState,connection: I32CFSP.ConnectfourConnection):
    ''' handle ai's message, return gamestate'''

    command=I32CFSP._read_line(connection).split()
    type=command[0]
    col=int(command[1])
    if type=='DROP':
        try:
            GameState=connectfour.drop(GameState,col-1)
            connectfour_common.display_board(GameState)
            return GameState
        except connectfour.GameOverError:
            return GameState
    elif type=='POP':
        GameState=connectfour.pop(GameState,col-1)
        connectfour_common.display_board(GameState)
        return GameState


def _ask_for_username() -> str:
    ''' ask for username '''
    while True:
        username = input('Username: ').strip()
        if len(username) > 0:
            return username
        else:
            print('That username is blank; please try again')

            
def choose_state(GameState:connectfour.GameState,connection:I32CFSP.ConnectfourConnection):
    '''hanle clients's command, return gamestate'''
    while True:
        n=connectfour_common.dop_or_pop()
        if n == 'drop':
            result=connectfour_common.choose_drop(GameState)
            GameState=result[0]
            I32CFSP._write_line(connection,"DROP "+str(int(result[1])))
            return GameState
            break
        elif n == 'pop':
            try:
                result=connectfour_common.choose_pop(GameState)
                GameState=result[0]
                I32CFSP._write_line(connection,"POP "+str(int(result[1])))
                return GameState
                break
            except:
                print("You can't pop in this column")
                choose_state(GameState)
        else:
            print('Invalid command, please enter drop or pop')
            continue       


if __name__ == '__main__':
    _run_user_interface()
    
