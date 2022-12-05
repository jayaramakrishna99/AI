import random
import emoji
from tabulate import tabulate
l=[["."]*3 for i in range(3)]
f=emoji.emojize(":victory_hand:")
s=emoji.emojize(":yellow_heart:")

def first(i,j):
    l[i][j]=f
    print(tabulate(l))

def second(i,j):
    l[i][j]=s
    print(tabulate(l))

def check():
    f1=[f,f,f]
    s1=[s,s,s]
    v1=[l[0][0],l[1][0],l[2][0]]
    v2=[l[0][1],l[1][1],l[2][1]]
    v3=[l[0][2],l[1][2],l[2][2]]
    x1=[l[0][0],l[1][1],l[2][2]]
    x2=[l[0][2],l[1][1],l[2][0]]
    if l[0]==f1 or l[0]==s1 or l[1]==f1 or l[1]==s1 or l[2]==f1 or l[2]==s1:
        return True
    if v1==f1 or v2==f1 or v3==f1 or v1==s1 or v2==s1 or v3==s1:
        return True
    if x1==f1 or x1==s1 or x2==f1 or x2==s1:
        return True
    else:
        return False
def duo():
    print("player 1 Vs player 2")
    for i in range(9):
        if i%2==0:
            print("player-1",f)
            l1=[int(i) for i in input("Enter the indices:").split()]
            first(l1[0],l1[1])
            if check()==True:
                print("First player is won")
                break
        else:
            print("plater-2",s)
            l2=[int(i) for i in input("Enter the indices:").split()]
            second(l2[0],l2[1])
            if check()==True:
                print("Second player is won")
                break


def check1(l2):
    l3=[random.randint(0,2),random.randint(0,2)]
    if (l3 in l2):
        l2.append(l3)
        return check1(l2)
    l2.append(l3)
    return l3

def sys():
    l2=[]
    print("computer vs player")
    for i in range(9):
        if i%2==0:
            l1=[int(i) for i in input("Enter the indices:").split()]
            l2.append(l1)
            first(l1[0],l1[1])
            if check()==True:
                print("player is won")
                break
        else:
            c=check1(l2)
            second(c[0],c[1])
            if check()==True:
                print("System won the game")
                break
print("1.2-player mode(Duo)\n2.1-player(computer)")
n=int(input("Enter for game mode:"))
print(tabulate(l))
if n==1:
    duo()
else:
    sys()