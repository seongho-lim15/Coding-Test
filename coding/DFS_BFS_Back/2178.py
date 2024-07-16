from  collections import deque

N, M = map(int, input().split())

que = deque()
chars = []
graph = [[] for _ in range(N)]
chk_graph = [[0]*M for _ in range(N)]
node_count = [[0]*M for _ in range(N)]

for idx in range(N):
    for char in input():
        chars.append(char)
        graph[idx].append(int(char))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def is_valid(y, x):
    if y > N-1 or y < 0 or x > M-1 or x < 0 or chk_graph[y][x] == 1 or graph[y][x] == 0:
        return False
    else:
        return True

count = 0
que.append((0,0))
chk_graph[0][0] = 1
node_count[0][0] = 1


while len(que) > 0:
    y, x = que.popleft()

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if is_valid(new_y, new_x):
            count = count + 1
            node_count[new_y][new_x] = node_count[y][x] + 1
            que.append((new_y, new_x))
            chk_graph[new_y][new_x] = 1
            if new_y == N-1 and new_x == M-1:
                # print(f'node_count : {node_count[new_y][new_x]}')
                print(node_count[new_y][new_x])


