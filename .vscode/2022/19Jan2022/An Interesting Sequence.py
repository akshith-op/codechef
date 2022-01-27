# cook your dish here
T = int(input())
for idx in range(T):
    j = 0
    A = []
    S = []
    K = int(input())
    pivot = K
    if K%2 == 1:
        print(0)
    else:
        while pivot%2 == 0:
            A.append(pivot//2)
            pivot = pivot//2
        for i in range(len(A)):
            S.append(sum(A[:i+1]))
        for i in range(len(A)):
            if A[i]+S[i] == K:
                j+=1
        if j == len(A):
            print(len(A))
    
    
