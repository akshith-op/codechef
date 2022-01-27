# cook your dish here
T = int(input())
for idx in range(T):
    ddsa,dtoc,ddm = map(int,input().split(" "))
    sdsa,stoc,sdm = map(int,input().split(" "))
    dragon = []
    dragon.append(ddsa)
    dragon.append(dtoc)
    dragon.append(ddm)
    sloth = []
    sloth.append(sdsa)
    sloth.append(stoc)
    sloth.append(sdm)
    if sum(dragon)>sum(sloth):
        print('Dragon')
    elif sum(dragon)< sum(sloth):
        print('Sloth')
    elif sum(dragon)==sum(sloth):
        if ddsa>sdsa:
            print('Dragon')
        elif ddsa<sdsa:
            print("Sloth")
        else:
            if dtoc>stoc:
                print('Dragon')
            elif dtoc<stoc:
                print("Sloth")
            else:
                print("Tie")



