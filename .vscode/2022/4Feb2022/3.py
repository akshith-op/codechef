# T = int(input())
# for i in range(T):


start = 0
steps = 0
n,k = map(int,input().split(" "))
end = n-1
string = str(input())
string = list(string)
rev_string = list(string[::-1])
while steps != k:
    if k == 0:
        if rev_string == string:
            print('Yes')
        else:
            print("No")
    if string[start] != string[end]:
        string[start] = string[end]
        steps+=1
        start +=1
        end-=1
        print(string)
        rev_string = list(string[::-1])
        print(rev_string)
    else:
        start+=1
        end-=1
if rev_string == string and steps == k:
    print("Yes")
else:
    print("No")