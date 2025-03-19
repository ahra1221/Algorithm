import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp != 0:
        heapq.heappush(heap, (abs(tmp), tmp))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")