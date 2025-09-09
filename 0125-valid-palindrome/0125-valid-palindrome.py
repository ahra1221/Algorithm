class Solution:
    def isPalindrome(self, s: str) -> bool:
        pharse = ""
        for i in s:
            if 97 <= ord(i.lower()) <= 122:
                pharse += i.lower()
        return (pharse == pharse[::-1])