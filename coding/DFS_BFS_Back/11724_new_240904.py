N,M = map(int, input().split(' '))

checkList = [0 for i in range(N)]
count = 0

for i in range(M):
    a, b = map(int, input().split(' '))

    if checkList[a - 1]:
        checkList[b - 1] = 1
    else:
        checkList[a - 1] = 1
        checkList[b - 1] = 1
        count += 1

print(count)


