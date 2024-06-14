import heapq as hq

N = int(input())
pq = []
arr = [int(input()) for _ in range(N)]

for elem in arr:
    if elem != 0:
        hq.heappush(pq, elem)
    elif elem == 0:
        if len(pq) != 0:
            print(hq.heappop(pq))
        else:
            print(0)

# from collections import deque
#
# de = deque()
#
# N = int(input())
# arr = [int(input()) for _ in range(N)]
#
# for elem in arr:
#     if elem != 0:
#         first_value = de.popleft()
#         if first_value < elem
#     elif elem == 0:
#         if len(de) != 0:
#             de.popleft()
#         else:
#             print(0)



