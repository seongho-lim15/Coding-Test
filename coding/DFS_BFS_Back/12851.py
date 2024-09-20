from collections import deque

N, K = map(int, input().split(' '))
que = deque()
prev_positions = [0] * 100001

que.append((N, 0, N))
prev_positions[N] = 1
correct_cnt = 0
correct_position_cnt = 0

while len(que) > 0:
    # 큐에서 값 꺼냄
    now_sts = que.popleft()

    # 현 위치가 K 인 값이 1개 이상 존재하고, 현재 위치의 시간이 최단 시간보다 길 때, 반복문 종료
    if correct_cnt > 0 and now_sts[1] > correct_position_cnt:
        # print(f'now_position : {now_position}')
        print(correct_position_cnt)
        print(correct_cnt)
        break

    # 현 위치가 K 가 되었을 때, correct_cnt 추가
    if now_sts[0] == K:
        # print(f'now_position : {now_sts}')
        correct_position_cnt =  now_sts[1]
        correct_cnt = correct_cnt + 1
    else:
        # 현재 위치
        now_pstn = now_sts[0]
        if 0<= now_pstn - 1 <= 100000 and prev_positions[now_pstn - 1] == 0:
            # 갈 수 있는 위치면, que 에 추가
            que.append((now_sts[0] - 1, now_sts[1] + 1, *now_sts[2:], now_sts[0] - 1))
            # 지나간 경로에 추가
            if now_pstn - 1 != K:
                prev_positions[now_pstn - 1] = 1

        if 0<= now_pstn + 1 <= 100000 and prev_positions[now_pstn + 1] == 0:
            que.append((now_sts[0] + 1, now_sts[1] + 1, *now_sts[2:], now_sts[0] + 1))
            if now_pstn + 1 != K:
                prev_positions[now_pstn + 1] = 1
        if 0<= now_pstn * 2 <= 100000 and prev_positions[now_pstn *2] == 0:
            que.append((now_sts[0] * 2, now_sts[1] + 1, *now_sts[2:], now_sts[0] * 2))
            if now_pstn *2 != K:
                prev_positions[now_pstn * 2] = 1