class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans = list(set(edges[0]) & set(edges[1]))
        return ans.pop()