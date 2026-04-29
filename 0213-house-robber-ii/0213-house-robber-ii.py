class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        #첫번째 포함
        prev1 = 0
        cur1 = 0
        for i in range(0, n-1):
            prev1,cur1 = cur1, max(prev1+nums[i], cur1)

        #첫번째 미포함
        prev2 = 0
        cur2 = 0
        for i in range(1, n):
            prev2,cur2 = cur2, max(prev2+nums[i], cur2)

        return max(cur1,cur2)
