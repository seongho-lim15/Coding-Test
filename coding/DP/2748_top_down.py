N = int(input())

dp_table = [-1] * (N+1)
dp_table[0] = 0
dp_table[1] = 1


def f(n):
    if dp_table[n] != -1:
        return dp_table[n]
    else:
        result = f(n-1) + f(n-2)
        dp_table[n] = result
        return result

print(f(N))

