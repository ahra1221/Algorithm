class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for n in nums:
            if (n-1) not in nums:
                cur = n
                l = 1
                while cur + 1 in nums:
                    cur += 1
                    l += 1
                ans = max(ans, l)
        return ans

                