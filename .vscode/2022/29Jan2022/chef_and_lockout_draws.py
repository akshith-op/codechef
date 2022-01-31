T = int(input())
for i in range(T):
    arr = list(map(int,input().split(" ")))
    arr = sorted(arr,reverse=True)
    if arr[0] == sum(arr[1:]):
        print('Yes')
    else:
        print("No")

