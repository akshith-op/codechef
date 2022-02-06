t = int(input())
for i in range(t):
    pivot_1 = 1
    pivot_0 = 0
    rooms = []
    value = 0
    cont = True
    index = 0
    x,y = map(int,input().split(" "))
    rooms.append(1)
    while cont:
        if y == 0:
            print(x)
        else:
            if rooms.count(1) == y:
                length = len(rooms)
                value+=length
                value+=x-y+1
                cont = False
                
            elif len(rooms)>=1:
                if rooms[index] == 1:
                    rooms.append(0)
                    index+=1
                else:
                    rooms.append(1)
                    index+=1
    print(value)
