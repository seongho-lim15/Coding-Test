N = int(input())
num_arr = list (map(int, input().split(' ')))

num_cnt = 0

for num in num_arr:
    if num != 1:
        is_prime = True
        for nanum in range(2, num):
            # print(f'num : {num }, nanum : {nanum}')
            if num % nanum == 0:
                is_prime = False
                break

        if is_prime:
            num_cnt +=1

print(num_cnt)



