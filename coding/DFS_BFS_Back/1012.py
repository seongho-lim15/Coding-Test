import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

move_x = [1,0,-1,0]
move_y = [0,1,0,-1]

for _ in range(T):

    M, N, K = map(int, sys.stdin.readline().split(' '))
    count = 0
    graph = [ [0]* M for _ in range(N) ]
    valid_graph = [ [0]* M for _ in range(N) ]

    # 배추 심기
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split(' '))
        graph[Y][X] = 1

    # 유효성 검사
    def is_valid(valid_y, valid_x):
        if 0 <= valid_y < N and 0 <= valid_x < M and valid_graph[valid_y][valid_x] == 0 and graph[valid_y][valid_x] == 1:
            return True
        else:
            return False

    # 재귀 함수
    def recur(now_y, now_x):
        for i in range(4):
            new_y = now_y + move_y[i]
            new_x = now_x + move_x[i]
            if is_valid(new_y, new_x):
                # print(f'new_y : {new_y}, new_x : {new_x}')
                valid_graph[new_y][new_x] = 1
                recur(new_y,new_x)

    # 실행
    for y in range(N):
        for x in range(M):
            if is_valid(y,x):
                recur(y,x)
                count = count + 1

    print(count)
