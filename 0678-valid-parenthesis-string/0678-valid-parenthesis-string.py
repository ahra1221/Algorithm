class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for p in s:
            if p == "(":
                low += 1
                high += 1
            elif p == ")":
                low -= 1
                high -= 1
            else: # "*"
                low -= 1
                high += 1
            low = max(low, 0)
            if high < 0:
                return False
        if low > 0:
            return False
        else:
            return True
