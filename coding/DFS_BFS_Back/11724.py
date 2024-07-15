from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(10**6)

N, M = map(int, stdin.readline().split(" "))
graph = [[0]*N for _ in range(N)]

for index in range(M):
    u, v = map(int, stdin.readline().split(" "))
    graph[u-1][v-1] = graph[v-1][u-1] = 1

chk_list = [-1] * N
count = 0

def dfs(node_idx):
    global count
    chk_list[node_idx] = 1

    for new_node_idx in range(N):
        if graph[node_idx][new_node_idx] == 1:
            if chk_list[new_node_idx] == -1:
                dfs(new_node_idx)

for index in range(N):
    if chk_list[index] == -1:
        count +=1
        dfs(index)

print(count)