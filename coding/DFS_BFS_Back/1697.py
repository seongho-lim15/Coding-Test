from collections import deque

N, K = map(int, input().split(' '))
que = deque()
pre_position = [0] * 100001

que.append((N, 0))
pre_position[N] = 1

while len(que) > 0:
    now_position = que.popleft()

    if now_position[0] == K:
        print(now_position[1])
        que = []
    else:
        now = now_position[0]
        if 0<= now - 1 <= 100000 and pre_position[now - 1] == 0:
            que.append((now - 1, now_position[1] + 1))
            pre_position[now - 1] = 1
        if 0<= now + 1 <= 100000 and pre_position[now + 1] == 0:
            que.append((now + 1, now_position[1] + 1))
            pre_position[now + 1] = 1
        if 0<= now * 2 <= 100000 and pre_position[now * 2] == 0:
            que.append((now * 2, now_position[1] + 1))
            pre_position[now * 2] = 1
