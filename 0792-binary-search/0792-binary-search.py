class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        en = len(nums)-1
        while st <= en:
            mid = (st+en) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                st = mid + 1
            else:
                en = mid -1
        return -1
