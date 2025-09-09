# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        st = 0
        en = n-1
        ans = 0
        while st <= en:
            mid = (st + en) // 2
            if isBadVersion(mid+1):
                ans = mid + 1
                en = mid - 1
            else:
                st = mid + 1
        return ans