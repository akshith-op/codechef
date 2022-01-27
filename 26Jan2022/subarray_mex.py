# cook your dish here
T = int(input())
for i in range(T):
    pivot = 0
    arr = []
    n,k,x = map(int,input().split(" "))
    if k < x:
        print(-1)
    elif k>=x:
        while len(arr) != n:
            if pivot == x:
                pivot = 0
            else:
                arr.append(pivot)
                pivot+=1
        arr_2 = [str(idx) for idx in arr] 
        print(" ".join(arr_2))
    

