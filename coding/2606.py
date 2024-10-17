import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())


check_graph = [[0]  * (N+1) for _ in range(N+1) ]
valid_graph = [0]  * (N+1)
count = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    check_graph[a][b] = check_graph[b][a] = 1

def recur(idx):
    global count
    valid_graph[idx] = 1

    for new_idx in range(1, N+1):
        if check_graph[idx][new_idx] == 1 and valid_graph[new_idx] == 0:
            count +=1
            # print(f'idx : {idx}, new_idx : {new_idx}')
            recur(new_idx)

recur(1)
print(count)



