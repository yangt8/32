# Yang Tang 53979886
import logic

def empty(x:list):
    choose=input()
    if choose=='Q':
        pass
    if choose[0]=='F':
        y=choose.split()
        bu=logic.buffer()
        choose_col=int(y[1])
        choose_letter=y[2:]
        col=x[choose_col].count(' 0 ')
        new_l=bu.move(choose_letter,choose_col,col)
        if new_l[1]==1:
            pass
        else:
            empty(new_l[0])

def contents(x:list,r:int):
    result=[]
    for i in range(r):
        n = input()
        result.append(n)
    for j in range(1,len(x)-1):
        for k in range(len(x[0])):
            if result[k][j-1]!=' ':
                x[j][k]=' ' +result[k][j-1]+' '
    for l in x:
        for u in l:
            if u == ' 0 ':
                l.remove(u)
    for l in x:
        for i in range(len(x[0])-len(l)):
            l.insert(0,' 0 ')
    logic.match(x)
    logic.display_board(x)
    empty(x)
    
def user_interface():
    BOARD_ROWS=int(input())
    BOARD_COLUMNS=int(input())
    situation=input()
    list_2d = [ [' 0 ' for i in range(BOARD_ROWS)] for i in range(BOARD_COLUMNS)]
    l=list('|'*BOARD_ROWS)
    list_2d.insert(0,l)
    list_2d.insert(BOARD_ROWS+2,l)
    logic.Jewel.board=list_2d
    if situation=='EMPTY':
        logic.display_board(list_2d)
        empty(list_2d)
        
    elif situation=='CONTENTS':
        contents(list_2d,BOARD_ROWS)

          
if __name__ == "__main__":
    user_interface()
