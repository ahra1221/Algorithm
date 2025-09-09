class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return(nums != sorted(list(set(nums))))