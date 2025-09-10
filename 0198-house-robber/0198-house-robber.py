class Solution:
    def rob(self, nums: List[int]) -> int:
        n =len(nums)
        if n < 1:
            return 0
        if n <= 2:
            return max(nums)
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]

        for i in range(3, n):
            tmp = max(dp[0:i-1])
            dp[i] = nums[i] + tmp
        return max(dp)
