import sys

N = int(sys.stdin.readline())
num_list = []
center_idx = 0
new_mid_idx = 0

# 이진 삽입 정렬 실행
def biInsertSort():

    # 이진 삽입 정렬 메소드
    def biInsert(num, mIdx, min_idx, max_idx):
        global center_idx, new_mid_idx

        if num <= num_list[mIdx]: # 입력된 값이 num_list 의 중간 값보다 작을 경우
            max_idx = mIdx
        elif num_list[mIdx] < num: # 입력된 값이 num_list 의 중간 값보다 클 경우
            min_idx = mIdx

        if max_idx == 0:
            num_list.insert(max_idx, num)
        elif min_idx == len(num_list) -1:
            num_list.append(num)
        elif min_idx == max_idx -1:
            num_list.insert(max_idx, num)
        else:
            if min_idx >=0 and max_idx >=0:
                new_mid_idx = (max_idx + min_idx) // 2
            elif min_idx >= 0 > max_idx:
                new_mid_idx = (len(num_list) + min_idx) // 2
            elif max_idx >= 0 > min_idx:
                new_mid_idx = max_idx // 2

            biInsert(num, new_mid_idx, min_idx, max_idx)

    # 반복 하면서 입력 값을 받고 이진 삽입 정렬 실행
    for i in range(N):
        input_num = int(sys.stdin.readline())

        # 맨 처음만 실행
        if len(num_list) == 0:
            num_list.append(input_num)
        else:
            # 최소, 최대 인덱스 초기화
            start_min_idx = -1
            start_max_idx = -1
            # 중간 인덱스 세팅
            center_idx = len(num_list) // 2
            # 이진 삽입 정렬 메소드 호출
            biInsert(input_num, center_idx, start_min_idx, start_max_idx)

biInsertSort()
for list_num in num_list:
    print(list_num)