class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for idx, n in enumerate(nums):
            need = target - n
            if need in ans:
                return [ans[need], idx]
            ans[n] = idx