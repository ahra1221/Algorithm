class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 3: return n
        heap = [1]
        heapq.heapify(heap)
        s = set()
        
        while True:
            tmp = heapq.heappop(heap)
            
            if tmp in s: continue

            s.add(tmp)

            if len(s) == n: return tmp
            
            heapq.heappush(heap, tmp*2)
            heapq.heappush(heap, tmp*3)
            heapq.heappush(heap, tmp*5)