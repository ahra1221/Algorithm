class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        st = 0
        en = len(nums)-1
        while st <= en:
            mid = (st+en) // 2
            if nums[mid] < target:
                st = mid + 1
            elif nums[mid] > target:
                en = mid -1
            else:
                return mid
        return st
            
            
