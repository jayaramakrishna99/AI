import emoji as e
r=e.emojize(":robot:")
c=e.emojize(":cloud:")
w=e.emojize(":T-Rex:")
l=[[r,c,"O",c],
    ["s","_",c,"_"],
    [w,"S,B,TG","O",c],
    ["S","_",c,"O"]]

def move(x,y):   
        
    if(x==1 and y==1):
        print("Lets make a move")
        return
    
    elif(x==1 and y==2):
        print("You have entered into the room of breeze !\n please make sure to go into the right direction: ")
        l=[["_",r,"O",c],
        ["S","_",c,"_"],
         [w,"S,B,TG","O",c],
         ["S","_",c,"O"]]
        order(l)
    
    elif(x==1 and y==3):
        print(" you have fallen into the PIT \nGAME OVER!")
        return
    
    elif(x==1 and y==4):
        print("invalid move")
        return
    
    elif(x==2 and y==1):
        print("BE Alert! Wumpus is near")
        l=[["_",c,"O",c],
        [r,"_",c,"_"],
         [w,"S,B,TG","O",c],
         ["S","_",c,"O"]]
        return
    
    elif(x==2 and y==2):
        print("You are near to the treasure\nplease make sure to go into the right direction: ")
        
        l=[["_",c,"O",c],
        ["S",r,c,"_"],
         [w,"S,B,TG","O",c],
         ["S","_",c,"O"]]
        order(l)
    
    elif(x==2 and y==3):
        print("Pit is near you! Please make sure to choose your move wisely: ")        
        l=[["_",c,"O",c],
        ["S","_",r,"_"],
         [w,"S","O",c],
         ["S","_",c,"O"]]
        order(l)
    
    elif(x==2 and y==4):
        print("Now you have entered into the blank closet\nhurry up to find the treasure")
        l=[["_",c,"O",c],
        ["S","_",c,r],
         [w,"S,B,TG","O",c],
         ["S","_",c,"O"]]
        order(l)
    
    elif(x==3 and y==1):
        print("GAME OVER!!")
        
    elif(x==3 and y==2):
        print("YOU WON!!")
        return

    elif(x==3 and y==3):
        print("You have fallen into the PIT")
        print("GAME over!!")

def order(l):
    for i in l:
        print(i)

n=int(input("n:"))
for i in range(n):
    x=int(input("X-pos:"))
    y=int(input("Y-pos:"))
    move(x,y)
order(l)