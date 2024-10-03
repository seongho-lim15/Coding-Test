N, M = map(int, input().split(' '))
card_arr = list(map(int, input().split(' ')))

max_num = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result = sum([card_arr[i], card_arr[j], card_arr[k]])
            if max_num<result<=M:
                max_num = result

print(max_num)