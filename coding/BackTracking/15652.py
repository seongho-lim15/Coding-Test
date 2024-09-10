N, M = map(int, input().split(' '))

stk = []

def recur(idx):
    stk.append(idx)

    if len(stk) == M:
        print(' '.join(map(str, stk)))
    else:
        for n_idx in range(idx, N+1):
            recur(n_idx)

    stk.pop()

for i in range(1, N+1):
    recur(i)