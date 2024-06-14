import heapq as hq
import sys
pq_plus = []
pq_minus = []
N = int(sys.stdin.readline())

for _ in range(N):
    input = int(sys.stdin.readline())
    if input == 0:
        if not pq_plus and not pq_minus:
            print(0)
        elif pq_plus and not pq_minus:
            print(hq.heappop(pq_plus))
        elif not pq_plus and pq_minus:
            print(-hq.heappop(pq_minus))
        else:
            min_plus = hq.heappop(pq_plus)
            min_minus = hq.heappop(pq_minus)

            if min_plus >= min_minus:
                print(-min_minus)
                hq.heappush(pq_plus, min_plus)
            elif min_plus < min_minus:
                print(min_plus)
                hq.heappush(pq_minus,min_minus)
    else:
        if input > 0:
            hq.heappush(pq_plus, input)
        else:
            hq.heappush(pq_minus, -input)
