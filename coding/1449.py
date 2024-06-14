
N, K = map(int, input().split())
place = list(map(int, input().split()))
place.sort()

count = 1
first_num = place[0]

# noinspection PyInterpreter
for i in range(N):
    if place[i] - first_num + 1 == K:
        if i != N - 1:
            count += 1
            first_num = place[i+1]

    elif place[i] - first_num + 1 > K:
        count += 1
        first_num = place[i]

print(count)
