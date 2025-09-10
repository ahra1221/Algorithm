class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        st = 0
        ans = 0
        for idx, string in enumerate(s):
            while string in window:
                window.remove(s[st])
                st += 1
            window.add(string)
            ans = max(ans, idx - st +1)
        return ans
            