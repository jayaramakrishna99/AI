x=0
y=0
x1=4
y1=3
while(x!=2):
    n=int(input())
    if(n==1):
        x=x1
    elif(n==2):
        y=y1
    elif(n==3):
        d=x1-x
        x=x1
        y=y-d
    elif(n==4):
        d=y1-y
        y=y1
        x=x-d
    elif(n==5):
        x=0
    elif(n==6):
        y=0
    elif(n==7):
        x=x+y
        y=0
    elif(n==8):
        y=y+x
        x=0
    print(x,y)
