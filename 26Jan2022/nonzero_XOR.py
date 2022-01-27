# cook your dish here
# cook your dish here
T = int(input())
for i in range(T):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(2**i)
    arrj = [str(idx) for idx in arr]
    print(" ".join(arrj))


