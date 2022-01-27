# cook your dish here
T = int(input())
for idx in range(T):
    sum = 0
    boxes = []
    N = int(input())
    r = list(input().split(' '))
    g = list(input().split(' '))
    b = list(input().split(' '))
    r = [int(x) for x in r]
    g = [int(x) for x in g]
    b = [int(x) for x in b]
    boxes.append(r)
    boxes.append(g)
    boxes.append(b)
    a = boxes[0][1]+boxes[0][2]+boxes[1][2]
    b = boxes[1][0]+boxes[2][0]+boxes[2][1]
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print(a)
    
