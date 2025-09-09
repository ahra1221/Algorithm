from collections import deque
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = deque()
        ans = float('-inf')
        s = 0
        for n in nums:
            window.append(n)
            s += n
            if len(window) == k:
                avg = s / k
                if avg > ans:
                    ans = avg
                tmp = window.popleft()
                s -= tmp
        return ans