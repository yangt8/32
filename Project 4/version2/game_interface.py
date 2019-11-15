
import game_logic
   
def build_the_board():
    row=int(input())
    col=int(input())
    choice=input()
    gamestate = game_logic.Gamestate(row, col)
    if choice=='EMPTY':
        gamestate.display_board()
        empty(gamestate)
    elif choice=='CONTENTS':
        contents(gamestate,row,col)


def command(Gamestate:game_logic.Gamestate):
    result=''
    while result!=3 and result!=4:
        com=input()           
        if com=='':
            result=Gamestate.falling()
        elif com=='R':
            result=Gamestate.rotate()
        elif com=='>':
            result=Gamestate.right()
        elif com=='<':
            result=Gamestate.left()
        elif com=='Q':
            result=4
        else:
            Gamestate.display_board()
    return result


def empty(Gamestate:game_logic.Gamestate):
    game=0
    while game!=4:
        com=input()
        if len(com)==1 and com=='Q':
            game=4
        elif com[0]=='F':
            n=com.split()
            col=int(n[1])
            colors=n[2:]
            Gamestate.fallers(colors)
            Gamestate.choose_col(col)
            Gamestate.falling()
            game=command(Gamestate)
            Gamestate._faller_state=-1
            Gamestate.position=-1
                
def contents(Gamestate:game_logic.Gamestate,row:int,col:int):
    result=[]
    for u in range(row):
        n = input()
        result.append(n)
    y=Gamestate._game_state
    for i in range(col):
        for j in range(row):
            if result[i][j]!=' ':
                y[j][i]=' '+result[i][j]+' '
    for l in y:
        for s in l:
            if s == ' 0 ':
                l.remove(s)
    for l in y:
        for m in range(row-len(l)):
            l.insert(0,' 0 ')
    Gamestate.match()
    Gamestate.display_board()
    empty(Gamestate)

def user_interface():
    build_the_board()

if __name__ == "__main__":
    user_interface()
