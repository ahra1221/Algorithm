class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtracking(curr)
                    curr.pop()
        backtracking([])
        return ans