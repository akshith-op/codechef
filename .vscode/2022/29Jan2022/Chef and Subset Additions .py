T = int(input())
for i in range(T):
    cont = True

    n,x,y = map(int,input().split(" "))
    a = list(map(int,input().split(" ")))
    b = list(map(int,input().split(" ")))
    for idx in range(n):
        if a[idx] == b[idx]:
            pass
        else:
            if a[idx]+x == b[idx]:
                cont = True
            else:
                cont = False
            if cont == False:
                if a[idx]+y == b[idx]:
                    pass
    if cont == False:
        print('No')
    else:
        print('Yes')            
        
