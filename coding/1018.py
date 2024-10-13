N, M = map(int, input().split(' '))

board_arr =[]
min_value = -1 # 예시의 최솟값
start_w = 0 # 흰색으로 시작했을 때 바꿔야하는 갯수
start_b = 0 # 검정색으로 시작했을 때 바꿔야하는 갯수

# 보드 배열 입력 받기
for _ in range(N):
    board_arr.append(input())

# 값 비교
for i in range(N-8 + 1): # 가능한 첫 행
    for j in range(M-8 + 1): # 가능한 첫 열
        # 값 초기화
        start_w = 0
        start_b = 0

        # 생성된 8X8 체크판 확인
        for k in range(8):
            for l in range(8):
                # 체스판 좌표가 짝수일 때,
                if (i + k + j + l) % 2 == 0:
                    # 값이 W 라면 black 으로 시작한 것은 바꿔야함
                    if board_arr[i+k][j+l] == 'W':
                        start_b +=1
                    # 값이 B 라면 white 으로 시작한 것은 바꿔야함
                    elif board_arr[i+k][j+l] == 'B':
                        start_w +=1
                # 체스판 좌표가 홀수일 때
                elif (i + k + j + l) % 2 == 1:
                    # 값이 B 라면 black 으로 시작한 것은 바꿔야함
                    if  board_arr[i+k][j+l] == 'B':
                        start_b +=1
                    # 값이 W 라면 white 으로 시작한 것은 바꿔야함
                    elif  board_arr[i+k][j+l] == 'W':
                        start_w +=1

        # 화이트로 시작한 것과 블랙으로 시작한 것 중, 변경 횟수가 더 적은 것을 선택
        # 그리고 현재 최솟값과 비교해서 현재 최솟값보다 더 적다면 최솟값 교체
        if start_w <= start_b:
            if start_w <= min_value or min_value == -1:
                min_value = start_w
        else:
            if start_b <= min_value or min_value == -1:
                min_value = start_b

# 최솟값 출력
print(min_value)