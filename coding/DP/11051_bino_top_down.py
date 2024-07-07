N, K = map(int, input().split(' '))
dp_table = [[-1] * (N + 1) for _ in range(N + 1)]
dp_table[0][0] = 1

for i in range(1, N + 1):
    dp_table[i][0] = dp_table[i][i] = 1

def bino(n, k):
    if dp_table[n][k] != -1:
        return dp_table[n][k]
    else:
        result = ( bino(n - 1, k) + bino(n - 1, k - 1) ) % 10007
        dp_table[n][k] = result
        return result

print(bino(N, K))
