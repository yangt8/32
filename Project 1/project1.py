# Yang Tang 53979886
from pathlib import Path
import os
import shutil

def find_files():
    result=[]
    n=input()
    try:
        if n[0]=='D' and len(n.split())!=1:
            p=list(Path(n[2:]).iterdir())
            for i in p:
                if i.is_file():
                    print(i)
                    result.append(i)
        elif n[0]=='R' and len(n.split())!=1:
            p=list(Path(n[2:]).iterdir())
            result=command_R(p)
            for i in command_R(p):
                print(i)
        else:
            print('ERROR')
            find_files()
    except:
        print('ERROR')
    search_characteristics(result)

           
def command_R(n:list)->list:
    result=[]
    for p in n:
        if p.is_file():
            result.append(p)
        elif p.is_dir():
            l=sorted(list(p.iterdir()))
            result.extend(command_R(l))      
    return result


def search_characteristics(l:list):
    n=input()
    inter_file=[]
    try:
        if n=='A':
            inter_file.extend(l)
            for i in inter_file:
                print(i)
        elif n[0]=='N' and len(n.split())!=1:
            if n[2:]=='':
                print('ERROR')
                search_characteristics(l)
            else:
                for i in l:
                    if n[2:]==i.name:
                        print(i)
                        inter_file.append(i)
        elif n[0]=='E' and len(n.split())!=1:
            if n[2:]=='':
                print('ERROR')
                search_characteristics(l)
            else:
                for i in l:
                    for j in i.suffixes:
                        if j.replace('.', '')==n[2:].replace('.', ''):
                            print(i)
                            inter_file.append(i)
        elif n[0]=='T' and len(n.split())!=1:
            for i in l:
                try:
                    f=open(i,'r')
                    if n[2:] in f.read():
                        print(i)
                        inter_file.append(i)
                    f.close()
                except:
                    pass
        elif n[0]=='<' and len(n.split())!=1:
            for i in l:
                if os.path.getsize(i)<int(n[2:]):
                    print(i)
                    inter_file.append(i)
        elif n[0]=='>' and len(n.split())!=1:
            for i in l:
                if os.path.getsize(i)>int(n[2:]):
                    print(i)
                    inter_file.append(i)
        else:
            print('ERROR')
            search_characteristics(l)
    except:
        print('ERROR')
    take_action_on_files(inter_file)



def take_action_on_files(l:list):
    n=input()
    try:
        if n=='F':
            for i in l:
                try:
                    f=open(i,'r')
                    print(f.readline().strip())
                    f.close()
                except:
                    print('NOT TEXT')
        elif n=='D':
            for i in l:
                new_path = str(i) + ".dup"
                shutil.copyfile(str(i),new_path)
                break
        elif n=='T':
            for i in l:
                i.touch()
                break
        else:
            print('ERROR')
            take_action_on_files(l)
    except:
        print('ERROR')



if __name__ == '__main__':
    find_files()
