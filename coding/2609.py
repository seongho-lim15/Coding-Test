import copy

N, M = map(int, input().split(' '))

min_common = 1
max_common = 1
# 최대 공약수 구하기
def solve_max_common():
    global max_common
    copy_N = copy.deepcopy(N)
    copy_M = copy.deepcopy(M)

    # 둘 중 더 작은 수로 나누기
    for i in range(2, min(N,M) +1):
        # 나눠야 되는 값이 나눠지는 값보다 크면 종료
        if i > copy_N or i > copy_M:
            break

        while True:
            if copy_N % i ==0 and copy_M % i ==0:
                max_common = max_common * i
                copy_N = copy_N // i
                copy_M = copy_M // i
            else:
                break

    print(max_common)

# 최소 공배수 구하기
def solve_min_common():
    global min_common

    # 최대 공약수가 없을 때는 두 수의 곱이 최소 공배수
    if max_common == 1:
        min_common = N * M
    else:
        min_common = max_common * (N // max_common) * (M // max_common)

    print(min_common)


# 최대 공약수 메소드 실행
solve_max_common()

# 최소 공배수 메소드 실행
solve_min_common()

