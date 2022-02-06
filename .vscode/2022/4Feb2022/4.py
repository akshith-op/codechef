T = int(input())
for i in range(T):
    value = 0
    cont = True
    index1 = 0
    n = int(input())
    arr = list(map(int,input().split(" ")))
    while cont:
        if n ==1:
            print(0)
        elif arr.count(arr[0]) == len(arr):
            print(0)
            cont = False
        elif n == 2:
            print(sum(arr))
        else:
            sum = 0
            sum += arr[index1]
            sum += arr[index1+1]
            arr.remove(arr[index1])
            arr.remove(arr[index1])
            arr.insert(index1,sum)
            value+=1
            index1+=1
            
            print(arr)




