from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(set(nums1))
        c2 = Counter(set(nums2))
        d = dict(c1+c2)
        keys = [k for k, v in d.items() if v >= 2]
        return keys
