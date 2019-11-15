#Yang Tang 53989886
import collections

Jewel=collections.namedtuple('Jewel', ['board','color','state'])
def display_board(x:list) -> None:
    ''' Displays the game state in the console. '''
    for j in range(len(x[0])):
        for i in range(len(x)):
            if x[i][j] == ' 0 ':
                print("   ", end = '')
            elif x[i][j] == '|':
                print("|", end = '')
            else:
                print(x[i][j], end = '')
        print()
    print(' '+'-'*((len(x)-2)*3)+' ')


class buffer():
    def land(self,choose_letter,choose_col,col):
        Jewel.state=='landed'
        for i in Jewel.board[choose_col]:
            if i[0] == '[':
                i2='|'+i[1]+'|'
                loc=Jewel.board[choose_col].index(i)
                Jewel.board[choose_col][loc]=i2
        return Jewel.board

    def frozen(self,choose_col):
        Jewel.state=='frozen'
        for i in Jewel.board[choose_col]:
            if i[0] == '|':
                i2=' '+i[1]+' '
                loc=Jewel.board[choose_col].index(i)
                Jewel.board[choose_col][loc]=i2
        match(Jewel.board)
        display_board(Jewel.board)
        return Jewel.board

 
    def move(self,choose_letter,choose_col,col:int):
        number=0
        Jewel.state=='move'
        for i in range(col):
            if Jewel.board[choose_col][i]==' 0 ':
                try:
                    if i==0:
                        Jewel.board[choose_col][0]='['+choose_letter[2]+']'
                        Jewel.color=choose_letter[2]
                        if Jewel.board[choose_col][1] == ' 0 ':
                            display_board(Jewel.board)
                            com=input()
                            if com=='Q':
                                number=1
                                break
                            else:
                                A=command(choose_letter,Jewel.board,choose_col,com,i)
                                choose_letter=A[0]
                                Jewel.board=A[1]
                                choose_col=A[2]
                        else:
                            bu=buffer()
                            n=bu.land(choose_letter,choose_col,col)
                    elif i==1:
                        Jewel.board[choose_col][1]='['+choose_letter[2]+']'
                        Jewel.color=choose_letter[2]
                        Jewel.board[choose_col][0]='['+choose_letter[1]+']'
                        Jewel.color=choose_letter[1]
                        if Jewel.board[choose_col][2] == ' 0 ':
                            display_board(Jewel.board)
                            com=input()
                            if com=='Q':
                                number=1
                                break
                            else:
                                A=command(choose_letter,Jewel.board,choose_col,com,i)
                                choose_letter=A[0]
                                Jewel.board=A[1]
                                choose_col=A[2]
                        else:
                            bu=buffer()
                            n=bu.land(choose_letter,choose_col,col)
                    elif i==2:
                        Jewel.board[choose_col][2]='['+choose_letter[2]+']'
                        Jewel.color=choose_letter[2]
                        Jewel.board[choose_col][1]='['+choose_letter[1]+']'
                        Jewel.color=choose_letter[1]
                        Jewel.board[choose_col][0]='['+choose_letter[0]+']'
                        Jewel.color=choose_letter[0]
                        if Jewel.board[choose_col][3] == ' 0 ':
                            display_board(Jewel.board)
                            com=input()
                            if com=='Q':
                                number=1
                                break
                            else:
                                A=command(choose_letter,Jewel.board,choose_col,com,i)
                                choose_letter=A[0]
                                Jewel.board=A[1]
                                choose_col=A[2]
                        else:
                            bu=buffer()
                            n=bu.land(choose_letter,choose_col,col)
                    elif col-1>i>=3:
                        Jewel.board[choose_col][i]='['+choose_letter[2]+']'
                        Jewel.color=choose_letter[2]
                        Jewel.board[choose_col][i-1]='['+choose_letter[1]+']'
                        Jewel.color=choose_letter[1]
                        Jewel.board[choose_col][i-2]='['+choose_letter[0]+']'
                        Jewel.color=choose_letter[0]
                        Jewel.board[choose_col][i-3]=' 0 '
                        if Jewel.board[choose_col][i+1] == ' 0 ':
                            display_board(Jewel.board)
                            com=input()
                            if com=='Q':
                                number=1
                                break
                            else:
                                A=command(choose_letter,Jewel.board,choose_col,com,i)
                                choose_letter=A[0]
                                Jewel.board=A[1]
                                choose_col=A[2]
                        else:
                            bu=buffer()
                            n=bu.land(choose_letter,choose_col,col)
                    elif i==col-1:
                        Jewel.state='landed'
                        Jewel.board[choose_col][i]='|'+choose_letter[2]+'|'
                        Jewel.color=choose_letter[0]
                        Jewel.board[choose_col][i-1]='|'+choose_letter[1]+'|'
                        Jewel.color=choose_letter[1]
                        Jewel.board[choose_col][i-2]='|'+choose_letter[0]+'|'
                        Jewel.color=choose_letter[2]
                        Jewel.board[choose_col][i-3]=' 0 '
                except:
                    pass
        if check_landed(Jewel.board,choose_letter,choose_col,col,i)==1:
            n=input()
            if n=='Q':
                number=1
            elif n=='R':
                command(choose_letter,Jewel.board,choose_col,n,i)
                bu=buffer()
                Jewel.state='frozen'
                bu.frozen(choose_col)
            else:
                bu=buffer()
                Jewel.state='frozen'
                bu.frozen(choose_col)
                if game_over(Jewel.board,choose_col,choose_letter)==1:
                    print('GAMEOVER')
                    number=1
        return Jewel.board,number

def game_over(x:list,choose_col,choose_letter):
    if x[choose_col].count(' 0 ')==0:
        return 1
        
def check_landed(x:list,choose_letter,choose_col:int,col,i):
    bu=buffer()
    if Jewel.board[choose_col][-1] != ' 0 ':
        new_l=bu.land(choose_letter,choose_col,col)
        display_board(new_l)
        return 1
    else:
        pass

def command(x:list,y:list,choose_col,com,i):
    if com=='':
        return (x,y,choose_col)
    elif com=='R':
        new_list=x[2]+x[0]+x[1]
        Jewel.board[choose_col][i]=Jewel.board[choose_col][i].replace(Jewel.board[choose_col][i][1],new_list[2])
        try:
            n=i-1
            m=i-2
            if n>=0:
                Jewel.board[choose_col][n]=Jewel.board[choose_col][n].replace(Jewel.board[choose_col][n][1],new_list[1])
            if m>=0:
                Jewel.board[choose_col][m]=Jewel.board[choose_col][m].replace(Jewel.board[choose_col][m][1],new_list[0])
        except:
            pass
        choose_col2=choose_col
        display_board(Jewel.board)
        com2=input()
        B=command(new_list,Jewel.board,choose_col2,com2,i)
        new_list=B[0]
        Jewel.board=B[1]
        choose_col2=B[2]
        return (new_list,Jewel.board,choose_col2)
    elif com=='>':
        if y[choose_col+1][i]==' 0 ':
            Z=right(y,choose_col,i)
            Jewel.board=Z[0]
            choose_col2=Z[1]
            display_board(Jewel.board)
        else:
            Jewel.board=y
            choose_col2=choose_col
        com2=input()
        B=command(x,Jewel.board,choose_col2,com2,i)
        new_list=B[0]
        Jewel.board=B[1]
        choose_col2=B[2]
        return (new_list,Jewel.board,choose_col2)
    elif com=='<':
        if y[choose_col-1][i]==' 0 ':
            Z=left(y,choose_col,i)
            Jewel.board=Z[0]
            choose_col2=Z[1]
            display_board(Jewel.board)
        else:
            Jewel.board=y
            choose_col2=choose_col
        com2=input()
        B=command(x,Jewel.board,choose_col2,com2,i)
        new_list=B[0]
        Jewel.board=B[1]
        choose_col2=B[2]
        return (new_list,Jewel.board,choose_col2)

    
def right(x,choose_col,i):
    for i in x[choose_col]:
        if i[0] != ' ':
            x[choose_col+1][x[choose_col].index(i)]=i
            x[choose_col][x[choose_col].index(i)]=' 0 '
            choose_col2=choose_col+1
    return (x,choose_col2)

def left(x,choose_col,i):
    for n in x[choose_col]:
        if n[0] != ' ':
            x[choose_col-1][x[choose_col].index(n)]=n
            x[choose_col][x[choose_col].index(n)]=' 0 '
            choose_col2=choose_col-1
    return (x,choose_col2)

def drop(x:list,i,j):
    x[i].remove(x[i][j].replace(' ','*'))
    x[i].insert(0,' 0 ')
        
def match(x:list):
    result=[]
    for i in range(1,len(x)-1):
        for j in range(len(x[0])):
            if x[i][j]==x[i+1][j]==x[i+2][j] and x[i][j]!=' 0 ':
                x[i][j]=x[i+1][j]=x[i+2][j]=x[i][j].replace(' ','*')
                display_board(x)
                n=input()
                drop(x,i,j)
                drop(x,i+1,j)
                drop(x,i+2,j)
                match(x)
            elif x[i][j-2]==x[i][j-1]==x[i][j] and x[i][j-2]!=' 0 ' and j-2>=0:
                x[i][j-2]=x[i][j-1]=x[i][j]=x[i][j-2].replace(' ','*')
                display_board(x)
                n=input()
                drop(x,i,j-2)
                drop(x,i,j-1)
                drop(x,i,j)
                match(x)
            elif x[i][j]==x[i+1][j-1]==x[i+2][j-2] and x[i][j]!=' 0 ':
                x[i][j]=x[i+1][j-1]=x[i+2][j-2]=x[i][j].replace(' ','*')
                display_board(x)
                n=input()
                drop(x,i,j)
                drop(x,i+1,j-1)
                drop(x,i+2,j-2)
                match(x)
            elif x[i][j]==x[i-1][j-1]==x[i-2][j-2] and x[i][j]!=' 0 ' and i-2>=0 and j-2>=0:
                x[i][j]=x[i-1][j-1]=x[i-2][j-2]=x[i][j].replace(' ','*')
                display_board(x)
                n=input()
                drop(x,i,j)
                drop(x,i-1,j-1)
                drop(x,i-2,j-2)
                match(x)
            else:
                pass
        
