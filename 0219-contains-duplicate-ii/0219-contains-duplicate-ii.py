class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, n in enumerate(nums):
            if n in window:
                return True
            window.add(n)
            if len(window) > k:
                window.remove(nums[i-k])
        return False