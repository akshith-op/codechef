# cook your dish here
T = int(input())
for i in range(T):
    people = []
    n,a = map(int,input().split(" "))
    people.append(a)
    people.append(n-a)
    if people[0]>=people[1]:
        print(n-a)
    elif people[0]<=people[1]:
        print(a)
    else:
        print(0)
        

