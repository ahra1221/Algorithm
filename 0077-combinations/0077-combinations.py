class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracking(idx, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for i in range(idx, n+1):
                if i not in curr:
                    curr.append(i)
                    backtracking(i+1,curr)
                    curr.pop()
        backtracking(1, [])
        return ans
        