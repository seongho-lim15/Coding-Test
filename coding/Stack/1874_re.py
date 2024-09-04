import sys

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n) ]
num_list.reverse()

num_stk = []
plus_minus_stk = []
count = 1
is_valid_flag = True

def check():
    global count, is_valid_flag

    while len(num_list) > 0 and is_valid_flag:
        pop_num = num_list.pop() # pop_num 은 4 ,3, 6, 8 ...

        # while num_stk[-1] != pop_num and is_valid_flag: # num_stk 는 1, 2, 3 ...
        while (not num_stk or num_stk[-1] != pop_num) and is_valid_flag: # num_stk 는 1, 2, 3 ...
            if count <= n :
                plus_minus_stk.append('+')
                num_stk.append(count)
                count += 1
            else:
                is_valid_flag = False

        if num_stk[-1] == pop_num:
            plus_minus_stk.append('-')
            num_stk.pop()

    if is_valid_flag:
        for ele in plus_minus_stk:
            print(ele)
    else:
        print('NO')

check()
# for _ in range(n):
#     if is_valid_flag:
#
#     if num_list.pop() == count:
#         plus_minus_stk.append('-')
#
#     elif count <= n :
#         plus_minus_stk.append('+')
#         count += 1
#     else:
#         is_valid_flag = False
