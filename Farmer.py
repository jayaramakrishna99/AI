print('Farmer=1\nWolf=2\nCabbage=3\nGoat=4')
l=[1,2,3,4]
print(l)
n=[]
while(n!=l):
    m=[int(i) for i in input().split(' ')]
    if(([1,4]==m or [4,1]==m)or ([1,3]==m or [3,1]==m) or ([1,2]==m or [2,1]==m) or ([1]==m)):
        if((([1,4]==m or [4,1]==m) and n==[]) or (([1,4]==m or [4,1]==m) and (n==[2,3] or n==[3,2])) or ([1]==m)):
            for i in m:
                n.append(i)
            for i in m:
                l.remove(i)
            print('Boat moving to ---> Right Side.')
            print(l,'--->',n)
        if(n!=[]):
            if(([1,3]==m or [3,1]==m) or ([1,2]==m or [2,1]==m)):
                for i in m:
                    n.append(i)
                for i in m:
                    l.remove(i)
                print('Boat moving to ---> Right side.')
                print(l,'--->',n)
        elif(([1,2]==m or [2,1]==m) or ([1,3]==m or [3,1]==m)):
            if(m==[1,2]):
                print('Goat had eaten cabbage.\nSo you failed to move.')
            else:
                print('Wolf had eaten goat.\nSo you failed to move.')
            break   
    else:
        print('With out Farmer boat cannot go.\nSo you failed to move.')
        break
    p=[int(i) for i in input().split(' ')]
    if(([1,4]==p or [4,1]==p) or ([1,3]==p or [3,1]==p) or ([1,2]==p or [2,1]==p) or ([1]==p)):
        if(([1]==p)  or ([1,4]==p or [4,1]==p)):
            for j in p:
                n.remove(j)
            for j in p:
                l.append(j)
            print('Boat moving to <---Left side.')
            print(l,'<--',n)
    else:
        print('With out Farmer boat cannot go.\nSo you failed to move.')
        break
