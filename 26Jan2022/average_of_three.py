# cook your dish here
T = int(input())
for i in range(T):
    arr = []
    x = int(input())
    large = x*3
    half = large//2
    if large%2 == 0:
        arr.append(half)
        arr.append(half-1)
        arr.append(1)
        arr_2 = [str(idx) for idx in arr ]
        print(" ".join(arr_2))
    elif large%2 == 1:
        large-=1
        odd_half = large//2
        arr.append(odd_half)
        arr.append(odd_half-1)
        arr.append(2)
        arr_2 = [str(idx) for idx in arr ]
        print(" ".join(arr_2))
        

