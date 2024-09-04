from collections import deque
from sys import stdin
# 그래프와 들린 곳을 체크할 그래프 2개의 2차원 배열이 필요 하다.

N, M = map(int, stdin.readline().split(' '))

# dy, dx 세팅
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# 큐 세팅
queue = deque()

# 그래프와 체크리스트 세팅
graph =[]
check_list = [[0]*M for i in range(N)]

for i in range(N):
    itemList =[]
    for j in input():
        itemList.append(int(j))

    graph.append(itemList)

# print(graph)


# 이동이 타당한 지 확인
def validation(new_y, new_x):
    if 0 <= new_y < N and 0 <= new_x < M:
        # print(f'valid new_y : {new_y}, new_x : {new_x}')
        if graph[new_y][new_x] == 1 and check_list[new_y][new_x] == 0:
            return True
        else:
            return False
    else:
        return False

# 그래프 위에서 이동
def moveToEnd(pre_y, pre_x):
    for i in range(4):
        new_y = pre_y + dy[i]
        new_x = pre_x + dx[i]

        # print(f'move new_y : {new_y}, new_x : {new_x}')

        if validation(new_y, new_x):
            queue.append((new_y, new_x))
            check_list[new_y][new_x] = check_list[pre_y][pre_x] + 1

# 이동 시작!
queue.append((0, 0))
check_list[0][0] = 1

while len(queue) != 0:
    (y,x) = queue.popleft()
    moveToEnd(y, x)

print(check_list[N-1][M-1])