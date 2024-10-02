import copy

N = int(input())
graph = []
valid_graph = [ [0]*N for _ in range(N)]
apart_count = 0
apart_list = []

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# 그래프 세팅
for _ in range(N):
    input_str = input()
    arr = list(map(int, input_str))
    graph.append(arr)

# 유효한 좌표인지 검증
def valid_position(y,x):

    if 0<= x < N and 0<= y < N and valid_graph[y][x]==0 and graph[y][x]==1:
        return True
    else:
        return False

# 재귀함수
def recur(y,x):
    global apart_count
    # 지나간 곳이라 체크
    valid_graph[y][x] = 1
    apart_count = apart_count + 1
    for k in range(4):
        new_y = y + dy[k]
        new_x = x + dx[k]
        if valid_position(new_y, new_x):
            recur(new_y, new_x)

# 실행
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and valid_graph[i][j]==0:
            apart_count = 0
            recur(i,j)
            apart_list.append(copy.deepcopy(apart_count))

# print(f'apart_list : {apart_list}, total_count : {total_count}')

print(len(apart_list))
for item in sorted(apart_list):
    print(item)

