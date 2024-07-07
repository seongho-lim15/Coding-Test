N, K = map(int, input().split(' '))
dp_table = [[-1] * (N + 1) for _ in range(N + 1)]
dp_table[0][0] = 1

for i in range(1, N + 1):
    dp_table[i][0] = dp_table[i][i] = 1

    for j in range(1, i):
        dp_table[i][j] = ( dp_table[i-1][j] + dp_table[i-1][j-1] ) % 10007

print(dp_table[N][K])




