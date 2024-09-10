import copy

N, M = map(int, input().split(' '))

num_arr = sorted(list(map(int, input().split(' '))))

stk = []
idx_stk = []
hstr_stk = []

def recur(idx):
    stk.append(num_arr[idx])
    idx_stk.append(idx)

    if len(idx_stk) == M:
        if stk not in hstr_stk :
            hstr_stk.append(copy.deepcopy(stk))
    else:
        for n_idx in range(N):
            if n_idx not in idx_stk:
                recur(n_idx)

    stk.pop()
    idx_stk.pop()

for i in range(N):
    recur(i)

for item_stk in hstr_stk:
    print(' '.join(map(str, item_stk)))



