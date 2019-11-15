# Yang Tang 53979886
import connectfour           
import connectfour_common

def main_game(GameveState:connectfour.GameState):
    '''
    main function of the game
    '''
    connectfour_common.welcome_banner()
    gamestate=connectfour.new_game()
    choose_state(gamestate)
                
def choose_state(GameState:connectfour.GameState):
    '''
    handle the command
    '''
    if connectfour_common.check_winner(GameState)==connectfour.NONE:
        turn(GameState)
        while True:
            n=connectfour_common.dop_or_pop()
            if n == 'drop':
                GameState=connectfour_common.choose_drop(GameState)[0]
                choose_state(GameState)
                break
            elif n=='pop':
                try:
                    GameState=connectfour_common.choose_pop(GameState)[0]
                    choose_state(GameState)
                    break
                except:
                    print('You can not pop in this column')
                    choose_state(GameState)
            else:
                print('Invalid command, please enter drop or pop')
                continue
    elif connectfour_common.check_winner(GameState)==connectfour.RED:
        print('RED WINS')
    elif connectfour_common.check_winner(GameState)==connectfour.YELLOW:
        print('YELLOW WINS')
        
        
def turn(GameState:connectfour.GameState):
    '''
    Given the player whose turn it is now
    '''
    print()
    if GameState.turn==connectfour.RED:
        print("Red's turn")
    elif GameState.turn==connectfour.YELLOW:
        print("Yellow's turn")
        
 
if __name__ == '__main__':
    main_game(connectfour.GameState)
