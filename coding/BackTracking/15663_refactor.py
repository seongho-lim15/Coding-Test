import copy

N, M = map(int, input().split(' '))
num_arr = sorted(list(map(int, input().split(' '))))

stk = []
idx_stk = []
hstr_stk = []

def recur():

    new_stk = []
    for idx in range(N):
        if idx not in idx_stk:
            if num_arr[idx] not in new_stk:
                stk.append(num_arr[idx])
                idx_stk.append(idx)
                new_stk.append(num_arr[idx])

                if len(idx_stk) == M:
                    hstr_stk.append(copy.deepcopy(stk))
                else:
                    recur()

                stk.pop()
                idx_stk.pop()

recur()

for item_stk in hstr_stk:
    print(' '.join(map(str, item_stk)))
