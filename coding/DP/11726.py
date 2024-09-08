import sys

sys.setrecursionlimit(10**8)

N = int(input())

tabul = [0] * N

tabul[0] = 1
if N >= 2:
    tabul[1] = 2

# 메모이제이션 사용
# def solveTabul(index):
#     if tabul[index]:
#         return tabul[index]
#     else:
#         tabul[index] = (solveTabul(index - 1 ) + solveTabul(index - 2 ))  % 10007
#         return tabul[index]

# 타뷸레이션 사용
if N > 2:
    for index in range(2, N):
        tabul[index] = (tabul[index - 1 ] + tabul[index - 2 ])  % 10007

print(tabul[N-1])
# print(solveTabul(N))
