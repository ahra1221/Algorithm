class Solution:
    def climbStairs(self, n: int) -> int:
        way = {1:1, 2:2}
        def climb(s):
            if s not in way:
                way[s] = climb(s-1) + climb(s-2)
            return way[s]
        climb(n)
        return way[n]