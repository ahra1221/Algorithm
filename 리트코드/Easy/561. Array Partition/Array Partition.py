class Solution(object):
    def arrayPairSum(self, nums):
        answer = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            answer += nums[i]
        return answer
