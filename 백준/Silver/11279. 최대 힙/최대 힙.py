import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp > 0:
        heapq.heappush(heap, -tmp)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print("0")