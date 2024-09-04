from sys import stdin
import sys

sys.setrecursionlimit(10**6)

N,M = map(int, stdin.readline().split(' '))

graph = [[0] * N for j in range(N)]
checkList = [0]* N
count = 0

# 그래프 작성
for i in range(M):
    a, b = map(int, stdin.readline().split(' '))
    a = a -1
    b = b -1
    graph[a][b] = 1
    graph[b][a] = 1


# 노드 체크
def check_node(index):
    # print(f'index : {index}')
    for j in range(N):
        if graph[index][j] == 1 and checkList[j] == 0:
            checkList[j] = 1
            check_node(j)


# 노드가 어디로 가는지 체크
for i in range(N):
    if checkList[i] == 0:
        count += 1
        check_node(i)

print(count)

