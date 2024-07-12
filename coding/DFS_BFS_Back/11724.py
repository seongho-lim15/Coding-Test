from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split(" "))
graph = [[0]*N for _ in range(N)]

for i in range(M):
    u, v = map(int, stdin.readline().split(" "))
    graph[u-1][v-1] = graph[v-1][u-1] = 1

def dfs():

    set_list = []
    count = 0
    q = deque()

    for i in range(N):
        q.append(i)
        chk = set()

        while len(q) > 0:
            node = q.popleft()
            chk.add(node)
            for i in range(N):
                if graph[node][i] == 1 and i not in chk :
                    q.append(i)
        # print(chk)
        if chk not in set_list:
            count += 1
            set_list.append(chk)

    return count

print(dfs())