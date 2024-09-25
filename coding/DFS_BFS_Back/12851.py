from collections import deque

N, K = map(int, input().split(' '))
que = deque()
prev_positions = [0] * 100001
cal_arr = ['-', '+', '*']

que.append((N, 0))
correct_cnt = 0
correct_position_cnt = 0

while que:
    # 큐에서 값 꺼냄
    now_sts = que.popleft()

    # # # 현 위치가 K 인 값이 1개 이상 존재하고, 현재 위치의 시간이 최단 시간보다 길 때, 반복문 종료
    # if correct_cnt > 0 and now_sts[1] > correct_position_cnt:
    #     print(correct_position_cnt)
    #     print(correct_cnt)
    #     break
    
    now_ps = now_sts[0]

    # 현 위치가 K 가 되었을 때, correct_cnt 추가
    if now_sts[0] == K:
        correct_position_cnt = prev_positions[now_ps]
        correct_cnt += 1
        continue

    for next_ps in [now_ps-1, now_ps+1, now_ps*2]:
        if 0 <= next_ps < 100001 and ( prev_positions[next_ps] == 0 or prev_positions[next_ps] == prev_positions[now_ps] + 1):
            # 갈 수 있는 위치면, que 에 추가
            que.append((next_ps, now_sts[1] + 1))

            # 지나간 경로에 추가
            # if next_ps != K:
            prev_positions[next_ps] = prev_positions[now_ps] + 1


print(correct_position_cnt)
print(correct_cnt)