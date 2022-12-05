import time
n=int(input("No.of locations: "))
print("Clean is 0 & Dirty is 1")
o=input("Do you want 'on' the vaccum cleaner?: ")
if(o=='on'):
    print("Starting Vaccum....in 4 seconds")
    time.sleep(4)
    p=[]
    q=[]
    r=[]
    for j in range(n):
        print("Would you like to go to the location?")
        m=input("Give 'yes' or 'no':")
        if(m=='yes'):
            for i in range(n):
                l=input("Name of location:")
                p.append(l)
                a=int(input("Location status:"))
                q.append(a)
                print("Location status of",l,"is",a)
                if a==1:
                    print("Sucking....the Location",l,"in 7 seconds")
                    time.sleep(7)
                    print(l,"is cleaned")
                    t=0
                    r.append(t)
                    time.sleep(2)
                elif a==0:
                    print(l,"is already cleaned")
                    time.sleep(2)
                    l=0
                    r.append(l)
                else:
                    print("Wrong input")
                break
        else:
            print("or for the another Location")
    print("Locations",p)
    print("Status of location before cleaning",q)
    print("Status of location after cleaning",r)
else:
    print("---")