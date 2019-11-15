
import collections

faller=collections.namedtuple('faller', ['position','color'])


not_start = -1
falling = 1
landed = 2
frozen = 3
game_over = 4

class Gamestate:
    def __init__(self, row: int, col: int):
        self._row = row
        self._col = col
        self._faller_state = -1
        self._game_state=[[' 0 ' for i in range(self._row)] for i in range(self._col)]
        self.position= -1
        self.jewel=['','','']
        self._choose_col=''
        self._third_faller = faller(self.position,self.jewel[2])
        self._second_faller = faller(self.position-1,self.jewel[1])
        self._first_faller = faller(self.position-2,self.jewel[0])
        

    def fallers(self,jewel: list):
        self.jewel=jewel
        self._first_faller = faller(self.position-2,jewel[0])
        self._second_faller = faller(self.position-1,jewel[1])
        self._third_faller = faller(self.position,jewel[2])

    def choose_col(self,col_num:int):
        self._choose_col = col_num
        
    
    def falling(self):
        self._faller_state = 1
        if self._game_state[self._choose_col-1].count(' 0 ') != 0 :
            self.position+=1
            try:
                if self._game_state[self._choose_col-1][self.position] == ' 0 ':
                    self._third_faller = faller(self.position,self.jewel[2])
                    self._game_state[self._choose_col-1][self.position] = self._third_faller.color
                    if self.position-1>=0:
                        self._second_faller = faller(self._third_faller.position-1,self.jewel[1])
                        self._game_state[self._choose_col-1][self.position-1] = self._second_faller.color
                        if self.position-2>=0:
                            self._first_faller = faller(self._third_faller.position-2,self.jewel[0])
                            self._game_state[self._choose_col-1][self.position-2] = self._first_faller.color
                            if self.position-3>=0:
                                self._game_state[self._choose_col-1][self.position-3] = ' 0 '
                Gamestate.landed(self)
                Gamestate.display_board(self)
            except:
                Gamestate.frozen(self)
        else:
            m=self._game_state[self._choose_col-1][0]
            if m[0]=='[':
                Gamestate.landed(self)
                Gamestate.display_board(self)
            elif self._first_faller.position==0:
                Gamestate.frozen(self)
            else:   
                Gamestate.frozen(self)
                print('GAME OVER')
            self._faller_state = 4
        return self._faller_state
    
                

    def landed(self):
        try:
            if self.position == self._row-1:
                self._faller_state = 2
            elif self._game_state[self._choose_col-1][self.position+1] != ' 0 ':
                self._faller_state = 2
            elif self._faller_state ==2:
                Gamestate.frozen(self)
        except:
            pass
        
            
    def frozen(self):
        self._faller_state = 3
        self.jewel=[' '+self.jewel[0]+' ',' '+self.jewel[1]+' ',' '+self.jewel[2]+' ']
        self._game_state[self._choose_col-1][self._third_faller.position] = self.jewel[2]
        self._game_state[self._choose_col-1][self._second_faller.position] = self.jewel[1]
        self._game_state[self._choose_col-1][self._first_faller.position] = self.jewel[0]
        Gamestate.match(self)
        Gamestate.display_board(self)


    def rotate(self):
        if self._faller_state != 3:
            self.jewel=[self.jewel[-1],self.jewel[0],self.jewel[1]]
            Gamestate.fallers(self,self.jewel)
            try:
                if self._third_faller.position>=0:
                    self._game_state[self._choose_col-1][self._third_faller.position] = self._third_faller.color
                if self._second_faller.position>=0:
                    self._game_state[self._choose_col-1][self._second_faller.position] = self._second_faller.color
                if self._first_faller.position>=0:
                    self._game_state[self._choose_col-1][self._first_faller.position] = self._first_faller.color
            except:
                pass
            Gamestate.display_board(self)
        else:
            Gamestate.display_board(self)
            return self._faller_state


        
    def left(self):
        if self._faller_state != 3 and self._game_state[self._choose_col-2][self._third_faller.position] == ' 0 ':
            try:
                self._game_state[self._choose_col-2][self._third_faller.position] = self._third_faller.color
                self._game_state[self._choose_col-1][self._third_faller.position] = ' 0 '
                if self._second_faller.position>=0:
                    self._game_state[self._choose_col-2][self._second_faller.position] = self._second_faller.color
                    self._game_state[self._choose_col-1][self._second_faller.position] = ' 0 '
                    if self._first_faller.position>=0:
                        self._game_state[self._choose_col-2][self._first_faller.position] = self._first_faller.color
                        self._game_state[self._choose_col-1][self._first_faller.position] = ' 0 '
            except:
                pass
            self._choose_col = self._choose_col-1
            Gamestate.display_board(self)
        else:
            Gamestate.display_board(self)
            return self._faller_state
        

    def right(self):
        if self._faller_state != 3 and self._choose_col!=len(self._game_state) and self._game_state[self._choose_col][self._third_faller.position] == ' 0 ':
            try:
                self._game_state[self._choose_col][self._third_faller.position] = self._third_faller.color
                self._game_state[self._choose_col-1][self._third_faller.position] = ' 0 '
                if self._second_faller.position>=0:
                    self._game_state[self._choose_col][self._second_faller.position] = self._second_faller.color
                    self._game_state[self._choose_col-1][self._second_faller.position] = ' 0 '
                    if self._first_faller.position>=0:
                        self._game_state[self._choose_col][self._first_faller.position] = self._first_faller.color
                        self._game_state[self._choose_col-1][self._first_faller.position] = ' 0 '
            except:
                pass
            self._choose_col = self._choose_col+1
            Gamestate.display_board(self)
        else:
            Gamestate.display_board(self)
            return self._faller_state

    def match(self):
        for i in range(len(self._game_state)):
            for j in range(len(self._game_state[0])):
                try:
                    if self._game_state[i][j]==self._game_state[i+1][j]==self._game_state[i+2][j]!=' 0 ':
                        self._game_state[i][j]=self._game_state[i+1][j]=self._game_state[i+2][j]=self._game_state[i][j].replace(' ','*')
                        Gamestate.display_board(self)
                        n=input()
                        Gamestate.disappear(self,i,j)
                        Gamestate.disappear(self,i+1,j)
                        Gamestate.disappear(self,i+2,j)
                    elif self._game_state[i][j]==self._game_state[i][j+1]==self._game_state[i][j+2]!=' 0 ':
                        self._game_state[i][j]=self._game_state[i][j+1]=self._game_state[i][j+2]=self._game_state[i][j].replace(' ','*')
                        Gamestate.display_board(self)
                        n=input()
                        Gamestate.disappear(self,i,j)
                        Gamestate.disappear(self,i,j+2)
                        Gamestate.disappear(self,i,j+2)
                    elif self._game_state[i][j]==self._game_state[i+1][j+1]==self._game_state[i+2][j+2]!=' 0 ':
                        self._game_state[i][j]=self._game_state[i+1][j+1]=self._game_state[i+2][j+2]=self._game_state[i][j].replace(' ','*')
                        Gamestate.display_board(self)
                        n=input()
                        Gamestate.disappear(self,i,j)
                        Gamestate.disappear(self,i+1,j+1)
                        Gamestate.disappear(self,i+2,j+2)
                    elif self._game_state[i][j]==self._game_state[i+1][j-1]==self._game_state[i+2][j-2]!=' 0 ':
                        self._game_state[i][j]=self._game_state[i+1][j-1]=self._game_state[i+2][j-2]=self._game_state[i][j].replace(' ','*')
                        Gamestate.display_board(self)
                        n=input()
                        Gamestate.disappear(self,i,j)
                        Gamestate.disappear(self,i+1,j-1)
                        Gamestate.disappear(self,i+2,j-2)
                    else:
                        pass
                except:
                    pass
                
    def disappear(self,i,j):
        self._game_state[i].remove(self._game_state[i][j])
        self._game_state[i].insert(0,' 0 ')
                
        

    def display_board(self):
        print(self._game_state)
        l=list('|'*self._row)
        new_list= [l]+ self._game_state+[l]
        for j in range(len(new_list[0])):
            for i in range(len(new_list)):
                n=new_list[i][j]
                if new_list[i][j]  == ' 0 ':
                    print("   ", end = '')
                elif new_list[i][j] == '|':
                    print(n,end='')
                else:
                    if len(new_list[i][j])==3:
                        print(new_list[i][j],end='')
                    else:
                        if self._faller_state == 1:
                            print('['+new_list[i][j],end=']')
                        elif self._faller_state == 2:
                            print('|'+new_list[i][j],end='|')
            print()
        print(' '+'-'*((len(new_list)-2)*3)+' ')


