from collections import deque
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)
        seen = set()
        for a,b in trust:
            if (a,b) in seen:
                continue
            seen.add((a,b))
            indegree[b] += 1
            outdegree[a] += 1
        print(indegree, outdegree)
        for x in range(1, n+1):
            if indegree[x] == n-1 and outdegree[x] == 0:
                return x
        return -1