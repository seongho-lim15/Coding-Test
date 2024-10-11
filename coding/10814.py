import heapq as hq
import sys

pq =[]
N = int(sys.stdin.readline())

for i in range(N):
    input_arr = list(sys.stdin.readline().split(' '))
    input_arr[0] = int(input_arr[0])
    input_arr[1] = input_arr[1].strip()
    input_arr.insert(1, i+1)
    hq.heappush(pq, input_arr)

while pq:
    name = hq.heappop(pq)
    print(f'{name[0]} {name[2]}')