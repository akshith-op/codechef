# cook your dish here
T = int(input())
for i in range(T):
    x,y,z = map(int,input().split(" "))
    spent = x*y
    recieved = x*z
    print(recieved-spent)