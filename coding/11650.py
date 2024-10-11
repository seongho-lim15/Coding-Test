import sys
import heapq as hq

N = int(sys.stdin.readline())
pq=[]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split(' '))
    pq.append((a, b))

pq.sort()
pq.reverse()

while len(pq)>0 :
    arr = pq.pop()
    print(f'{arr[0]} {arr[1]}')

