import sys
N = int(sys.stdin.readline())
num_list = []

# 비겁 정렬
def normalSort():
    for i in range(N):
        input_num = int(sys.stdin.readline())
        num_list.append(input_num)

    num_list.sort()

    for num in num_list:
        print(num)

normalSort()

# 삽입 정렬
def insertSort():
    for i in range(N):
        input_num = int(sys.stdin.readline())

        if i == 0:
            num_list.append(input_num)
        else:
            is_small=False
            for num_idx in range(len(num_list)):
                if input_num < num_list[num_idx]:
                    num_list.insert(num_idx, input_num)
                    is_small = True
                    break

            if not is_small:
                num_list.append(input_num)

    for num in num_list:
        print(num)

# # 이진 삽입 정렬
# def biInsertSort():
#     def biInsert(idx):
#
#     for i in range(N):
#         input_num = int(sys.stdin.readline())
#
#         if i == 0:
#             num_list.append(input_num)
#         else:
#             num_mid_idx = len(num_list)//2
#
#             # num_list 의 중간 값이 들어온 값보다 작을 경우
#             if num_list[num_mid_idx] < input_num:
#
#             elif num_list[num_mid_idx] > input_num: # num_list 의 중간 값이 들어온 값보다 작을 경우
#
#     for num in num_list:
#         print(num)
