from operator import index
import numpy as np
a = np.array([])
l = [int(i) for i in input().split()]
# l=[2, 8, 3, 1, 6, 4, 7, 0, 5]
g = np.array([[1,2,3], [8,0,4], [7, 6,5]])
a = np.append(a, l)
a = a.reshape(3, 3)
print(['r','u','l','d'])
def mis_placed(b):
    c = 0
    for i in range(3):
        for j in range(3):
            if b[i][j] != g[i][j]:
                c += 1
    return c
print(mis_placed(a))

def right(y,l1,returnNew=False):
    b=a.copy()
    i, j = y
    b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
    b1=mis_placed(b)
    l1[0]=b1
    print(b)
    if returnNew:
        return b
    
def up(y,l1,returnNew=False):
    i, j = y
    b=a.copy()
    b[i][j], b[i - 1][j] = b[i - 1][j], b[i][j]
    b1=mis_placed(b)
    l1[1]=b1
    print(b)
    if returnNew:
        return b

def left(y,l1,returnNew=False):
    i, j = y
    b=a.copy()
    b[i][j], b[i][j - 1] = b[i][j - 1], b[i][j]
    b1=mis_placed(b)
    l1[2]=b1
    print(b)
    if returnNew:
        return b

def down(y,l1,returnNew=False):
    i, j = y
    b=a.copy()
    b[i][j], b[i + 1][j] = b[i + 1][j], b[i][j]
    b1=mis_placed(b)
    l1[3]=b1
    print(b)
    if returnNew:
        return b

def mini(l1):
    global a
    l2=l1.index(min(l1))
    print(l2)
    if l2==0:
        r=right(y,l1,True)
        a=r.copy()
        move(a)
    elif(l2==1):
        u=up(y,l1,True)
        a=u.copy()
        move(a)
    elif(l2==2):
        l=left(y,l1,True)
        a=l.copy()
        move(a)
    elif(l2==3):
        d=down(y,l1,True)
        a=d.copy()
        move(a)
    

# 2 8 3 1 6 4 7 0 5
# 2 8 3
# 1 6 4
# 7 0 5
def move(a):
    global y
#    while(a.all()!=g.all()):
    if mis_placed(a)!=0:
        x = np.where(a == 0)
        if x == (2, 1):
            l1 = [99,99,99,99]
            y = (2, 1)
            left(y,l1)
            up(y,l1)
            right(y,l1)     
            print(l1)
            mini(l1)            
        elif x == (0, 0):
            l1 = [99,99,99,99]
            y=(0,0)
            right(y,l1)
            down(y,l1)
            print(l1)
            mini(l1)
        elif x == (0, 1):
            l1 = [99,99,99,99]
            y=(0,1)
            left(y,l1)
            right(y,l1)
            down(y,l1)
            print(l1)
            mini(l1)
        elif x == (0, 2):
            l1 = [99,99,99,99]
            y = (0,2)
            left(y,l1)
            down(y,l1)
            mini(l1)
        elif x == (1, 0):
            l1 = [99,99,99,99]
            y = (1,0)
            right(y,l1)
            up(y,l1)
            down(y,l1)
            mini(l1)
        elif x == (1, 1):
            l1 = [99,99,99,99]
            y = (1,1)
            right(y,l1)
            up(y,l1)
            left(y,l1)
            down(y,l1)
            print(l1)
            mini(l1)
        elif x == (1, 2):
            l1 = [99,99,99,99]
            y = (1,2)
            up(y,l1)
            left(y,l1)
            down(y,l1)
            mini(l1)
        elif x == (2, 0):
            l1 = [99,99,99,99]
            y = (2,0)
            right(y,l1)
            up(y,l1)
            mini(l1)
        elif x == (2, 2):
            l1 = [99,99,99,99]
            y = (2,2)
            up(y,l1)
            left(y,l1)
            mini(l1)
    else:
        print("Goal Reached.")
move(a)