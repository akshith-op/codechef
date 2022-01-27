# cook your dish heret 
import statistics
t= int(input())
for i in range(t):
    n = int(input())
    p = []
    q = []
    j = []
    h = []
    arr = list(input().split(" "))
    arr = sorted(arr,reverse = True)
    if n%2 == 0:
        pivot = n//2
        p.append(arr[:pivot])
        q.append(arr[pivot:])
        for u in p:
            for idx in u:
                j.append(int(idx))
        for u in q:
            for idx in u:
                h.append(int(idx))
        x = statistics.mean(j)
        y = statistics.mean(h)
        print(x+y)
    else:
        pivot = n//2
        p.append(arr[:pivot])
        q.append(arr[pivot:])
        for u in p:
            for idx in u:
                j.append(int(idx))
        for u in q:
            for idx in u:
                h.append(int(idx))
        x = statistics.mean(j)
        y = statistics.mean(h)
        print(x+y)
        

        

