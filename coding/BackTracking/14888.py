import copy
import sys

N = int(sys.stdin.readline())
# 연산에 사용될 숫자를 저장
num_arr = list(map(int,sys.stdin.readline().split(' ')))
# 연산에 사용될 연산자를 저장
cal_arr = list(map(int,sys.stdin.readline().split(' ')))

# 연산된 결과를 순서대로 저장
rst_stk =[]
# 최종 연산된 결과를 저장
rst_hst_stk=[]

def recur():

    for i in range(4):
        if cal_arr[i]:
            if i == 0:
                rst = rst_stk[-1] + num_arr[len(rst_stk)]
            elif i == 1:
                rst = rst_stk[-1] - num_arr[len(rst_stk)]
            elif i == 2:
                rst = rst_stk[-1] * num_arr[len(rst_stk)]
            elif i == 3:
                # 이전 연산 값이 음수일 경우
                if rst_stk[-1] < 0:
                    rst = (rst_stk[-1] // -num_arr[len(rst_stk)]) * -1
                # 이전 연산 값이 양수일 경우
                else:
                    rst = rst_stk[-1] // num_arr[len(rst_stk)]

            # 연산에 사용한 부호 갯수 차감
            cal_arr[i] = cal_arr[i] - 1
            # 연산된 결과 값을 rst 스택에 저장
            rst_stk.append(rst)

            # rst_stk 스택의 길이가 N 일 경우 연산자를 다 쓴 것임 == 결과 값을 rst_hst_stk 스택에 저장
            if len(rst_stk) == N:
                rst_hst_stk.append( copy.deepcopy(rst_stk[-1] ) )
            else:
                recur()

            # 연산에 사용한 부호 갯수 복구
            cal_arr[i] = cal_arr[i] + 1
            # 연산된 결과 값을 rst 스택에서 꺼냄
            rst_stk.pop()

# 실행
rst_stk.append(num_arr[0])
recur()

print(max(rst_hst_stk))
print(min(rst_hst_stk))