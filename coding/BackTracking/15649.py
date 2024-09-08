N, M = map(int, input().split(' '))

stk = []

def recur(idx):

    # 1
    stk.append(idx)

    # 2
    if len(stk) == M:
        print(*stk)
    # 3
    else:
        for n_idx in range(1, N+1):
            if n_idx not in stk:
                recur(n_idx)

    # 4
    stk.pop()

for i in range(1, N+1):
    recur(i)

