#
#  Author: Tai Karir
#  First commit: 09/29/2020
#  Latest update: 15/10/2020
#  Email: tai.karir@gmail.com
#
import random
#dimensions of the game board
dimx=9
dimy=9
#number of hidden mines
mineCount=""
while not mineCount.isnumeric():
    mineCount=input("Number of mines? ")
mineCount=int(mineCount)
#array containing which tiles are known
known=[]
#array containing which tiles have mines
mines=[]
#setting up the arrays
for i in range(0,dimx):
    known.append([])
    mines.append([])
    for j in range(0,dimy):
        known[i].append(0)
        mines[i].append(0)
#this function returns the number of mines in the tiles adjacent to a given tile
def checkAdjacent(i,j):
    p=0
    if known[i][j]==1:
        if i>0:
            if j>0:
                p+=mines[i-1][j-1]
            if j<dimx-1:
                p+=mines[i-1][j+1]
            p+=mines[i-1][j]
        if i<dimy-1:
            if j>0:
                p+=mines[i+1][j-1]
            if j<dimx-1:
                p+=mines[i+1][j+1]
            p+=mines[i+1][j]
        if j>0:
            p+=mines[i][j-1]
        if j<dimx-1:
            p+=mines[i][j+1]
    return p
#this function automatically uncovers all surrounding tiles of a given tile if there are no mines there
def uncoverZeroes(known):
    while True:
        adj=0
        for i in range(0,dimy):
            for j in range(0,dimx):
                if known[i][j]==1:
                    if checkAdjacent(i,j)==0:
                         for i2 in range(i-1,i+2):
                             for j2 in range(j-1,j+2):
                                 if i2>=0 and i2<=dimy-1 and j2>=0 and j2<=dimx-1:
                                     if known[i2][j2]==0:
                                         known[i2][j2]=1
                                         adj+=1
        if adj==0:
            break
    return known
#prints the current game state based on which tiles are known
def prtscr():
    print("\n")
    d="       "
    for i in range(0,dimx):
        d+=str(i);d+="    "
    print(d);print("\n\n")
    for i in range(0,dimy):
        d=""
        d+=str(i);d+="      "
        for j in range(0,dimx):
            if known[i][j]==0:
                d+="?"
            elif known[i][j]==1:
                p=checkAdjacent(i,j)
                d+=str(p)
            elif known[i][j]==2:
                d+="F"
            d+="    "
        print(d+"\n\n")
#this function sets up the mines, making sure no mines are on the initial uncovered tile
def setUpMines(mines,known):
    dx=int(input("initx "))
    dy=int(input("inity "))
    for i in range(dx-1,dx+2):
        for j in range(dy-1,dy+2):
            known[i][j]=1
    for i in range(0,mineCount):
        while True:
            x=random.randrange(0,dimy)
            y=random.randrange(0,dimx)
            if (x==dx or x==dx-1 or x==dx+1) and (y==dy or y==dy-1 or y==dy+1):
                pass
            elif mines[y][x]!=1:
                mines[y][x]=1
                break
    known=uncoverZeroes(known)
    return mines,known
#what happens when you choose a tile
def clickedOn(known,x,y,flag):
    #uncovers a tile
    if flag==0:
        if mines[y][x]==1:
            known[y][x]=1
        elif mines[y][x]==0 and known[y][x]==0:
            known[y][x]=1
            known=uncoverZeroes(known)
    #places a flag
    else:
        if known[y][x]==0:
            known[y][x]=2
        elif known[y][x]==2:
            known[y][x]=0
    return known
#checks if you have reached the win or lose state
def checkWin():
    l=0
    for i in range(0,dimy):
        for j in range(0,dimx):
            if bool(mines[i][j]==1) != bool(known[i][j]==1):
                l+=1
            if known[i][j]==1 and mines[i][j]==1:
                return "Over"
    if l==dimx*dimy:
        return True
    else:
        return False
mines,known=setUpMines(mines,known)
prtscr()
#the main loop
while True:
    print("=============")
    fx="";fy="";flag=""
    while not fx.isnumeric():
        fx=input("x? ")
    while not fy.isnumeric():
        fy=input("y? ")
    while not flag.isnumeric():
        flag=input("flag? ")
    fx=int(fx);fy=int(fy);flag=int(flag)
    known=clickedOn(known,fx,fy,flag)
    if checkWin()==True:
        print("Congrats! You win!")
        break
    elif checkWin()=="Over":
        print("You lost.")
        break
    prtscr()
