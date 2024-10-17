import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
num_arr = list(map(int, sys.stdin.readline().strip().split(' ')))
memo_sum = [0] * N

for i in range(N):
    memo_sum[i] = memo_sum[i-1] + num_arr[i]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    a -=1
    b -=1
    if a == 0:
        print(memo_sum[b])
    else:
        print(memo_sum[b] - memo_sum[a-1])
