import copy
import sys

N = int(sys.stdin.readline())
num_arr = list(map(int,sys.stdin.readline().split(' ')))
cal_arr = list(map(int,sys.stdin.readline().split(' ')))

rst_stk =[]
rst_hst_stk=[]
recur_count = 0

def recur():
    global recur_count

    for i in range(4):
        if cal_arr[i]:

            if i == 0:
                rst = rst_stk[-1] + num_arr[recur_count + 1]
            elif i == 1:
                rst = rst_stk[-1] - num_arr[recur_count + 1]
            elif i == 2:
                rst = rst_stk[-1] * num_arr[recur_count + 1]
            elif i == 3:
                # 이전 연산 값이 음수일 경우
                if rst_stk[-1] < 0:
                    rst = (rst_stk[-1] // -num_arr[recur_count + 1]) * -1
                else:
                    rst = rst_stk[-1] // num_arr[recur_count + 1]

            cal_arr[i] = cal_arr[i] - 1
            rst_stk.append(rst)
            recur_count = recur_count + 1

            if len(rst_stk) == N:
                rst_hst_stk.append( copy.deepcopy(rst_stk[-1] ) )
            else:
                recur()

            recur_count = recur_count - 1
            rst_stk.pop()
            cal_arr[i] = cal_arr[i] + 1

# 실행
rst_stk.append(num_arr[0])
recur()

print(max(rst_hst_stk))
print(min(rst_hst_stk))





