import sys

input_arr = sys.stdin.readline().split(' ')

index = int(input_arr[0])
money = int(input_arr[1])

arr = []

# 입력 값들을 arr 에 저장
for i in range(index):
    arr.append(int(sys.stdin.readline()))

arr.reverse()

ans = 0
for coin in arr:
    ans += money // coin
    money = money % coin
print(ans)
