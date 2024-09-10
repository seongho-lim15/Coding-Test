import sys

def backtracking(num):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return    # 이는 return None과 같다.

    for i in range(num, N + 1):
        arr.append(i)
        backtracking(arr[-1] + 1)
        arr.pop()

N, M = map(int, sys.stdin.readline().split())
arr = []
backtracking(1)