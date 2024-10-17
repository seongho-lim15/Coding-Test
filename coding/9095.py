T = int(input())
memoi = [0] * 11
memoi[1] = 1
memoi[2] = 2
memoi[3] = 4

def solveMemoi(N):
    if memoi[N]:
        return memoi[N]
    else:
        memoi[N] = solveMemoi(N-1) + solveMemoi(N-2) + solveMemoi(N-3)
        return memoi[N]

for _ in range(T):
    N = int(input())

    print(solveMemoi(N))


