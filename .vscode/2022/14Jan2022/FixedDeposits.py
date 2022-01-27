# cook your dish here
T = int(input())
for idx in range(T):
    pivot = 0
    SUM = 0
    CONT = True
    value = []
    n,x = map(int,input().split(" "))
    a = list(input().split(" "))
    value = [int(x) for x in a]
    value = sorted(value,reverse = True)
    if x > sum(value):
        print(-1)
    elif x == sum(value):
        print(n)
    else:
        for g in value:
            if g >=x:
                print(1)
                CONT = False
                break
        while CONT == True:
            for jhu in value:
                SUM+=jhu
                pivot+=1
                if SUM >= x:
                    CONT = False
                    print(pivot)
                    break

        
        
        
    

