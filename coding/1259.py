result_arr = []
is_palin=True

while True:
    num_arr = list(map(int, input()))

    # 0 이 나오면 종료
    if num_arr[0] ==0:
        break

    is_palin=True
    arr_len = len(num_arr)

    # 길이가 짝수인 배열일 때
    if arr_len % 2 == 0:
        for i in range(arr_len//2):
            if num_arr[i] != num_arr[arr_len-1-i]:
                is_palin = False
    else:
        for i in range(arr_len//2):
            if num_arr[i] != num_arr[arr_len-1-i]:
                is_palin = False

    if is_palin:
        result_arr.append('yes')
    else:
        result_arr.append('no')


for result in result_arr:
    print(result)
