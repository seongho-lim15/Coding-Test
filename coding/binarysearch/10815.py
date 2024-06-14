from bisect import bisect_left, bisect_right

N = int(input())
NArr = sorted(list(map(int, input().split())))
M = int(input())
MArr = list(map(int, input().split()))
result =[]

# print(f'N : {N}, M : {M}, NArr : {NArr} ,MArr : {MArr} ')

for i in range(M):
    if bisect_right(NArr,MArr[i]) - bisect_left(NArr, MArr[i]) == 0:
        result.append(0)
    else:
        result.append(1)

print(*result)