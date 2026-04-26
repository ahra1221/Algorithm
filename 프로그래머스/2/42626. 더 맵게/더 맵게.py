import heapq
def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)
    
    while len(heap) >= 2 and heap[0] < K:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b*2)
        answer += 1
    
    if heap[0] >= K: return answer
    return -1