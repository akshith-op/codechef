for i in range(int(input())):
    n = 0
    p = int(input())
    if p>=1:
        for i in range(p+1):
            if i  %2 == 0:
                n +=1
        print(n)
    else:
        print(0)