import sys
import heapq

input = sys.stdin.readline
K,N = map(int, input().split())
primes = list(map(int, input().split()))

heap = primes[:]
heapq.heapify(heap)

for _ in range(N):
    val = heapq.heappop(heap)

    for p in primes:
        heapq.heappush(heap, val * p)
        
        if val % p == 0:
            break

print(val)