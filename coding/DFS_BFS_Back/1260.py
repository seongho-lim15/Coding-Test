from sys import stdin
from collections import deque

N, M, V = map(int, stdin.readline().split(' '))
graph = [[0] *N for _ in range(N)]

# dfs 변수 세팅
dfs_value_queue = deque()
dfs_check_list = [0] * N

# bfs 변수 세팅
bfs_check_graph = [[0]*N for _ in range(N)]
bfs_queue = deque()
bfs_check_list = [0] * N

for _ in range(M):
    node_a, node_b = map(int, stdin.readline().split(' '))
    node_a, node_b = node_a - 1, node_b - 1

    graph[node_a][node_b] = 1
    graph[node_b][node_a] = 1

# for items in graph:
#     for item in items:
#         print(item, end=' ')
#     print()

# dfs 메소드
def dfs(index):
    dfs_check_list[index] = 1
    print(index+1, end=' ')
    # dfs_value_queue.append(index+1)

    for node_i in range(N):
        if graph[index][node_i] == 1 and dfs_check_list[node_i] == 0:
            dfs(node_i)

# while len(dfs_value_queue) > 0:
#     print(dfs_value_queue.popleft(), end=' ')

# bfs 메소드
def bfs(start_node):
    bfs_queue.append(start_node)
    bfs_check_list[start_node] = 1

    while len(bfs_queue) > 0:
        bfs_item = bfs_queue.popleft()

        print(bfs_item + 1, end=' ')

        for node_i in range(N):
            if graph[bfs_item][node_i] == 1 and bfs_check_list[node_i] == 0:
                bfs_check_list[node_i] = 1
                bfs_queue.append(node_i)


# dfs 실행
dfs(V-1)
print()
# bfs 메소드 실행
bfs(V-1)