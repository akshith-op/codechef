# cook your dish here
T = int(input())
for i in range(T):
    parties = []
    major = []
    A,B,C = map(int,input().split(' '))
    values = {}
    parties.append(A)
    parties.append(B)
    parties.append(C)
    values["A"] = A
    values["B"] = B
    values["C"] = C
    
    for idx in parties:
        if idx>50:
            major.append(idx)
    if len(major)<1:
            print('NOTA')
        
    if len(major)>=1:
        for k, v in values.items():
            if v == max(major):
                print(k)
                
        
        
    

