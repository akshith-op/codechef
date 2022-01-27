# cook your d(ish here
T = int(input())
for i in range(T):
    pizza = True
    values = []
    x,y,z = map(int,input().split())
    if x>=z or x>=y:
        if x>=y:
            print("Pizza")
        else:
            pizza = False
        if x>=z:
            if pizza == False:
                print("Burger")
    else:
        print("Nothing")
        
    


