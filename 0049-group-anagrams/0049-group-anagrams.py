class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        col = {}
        idx = 0
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp in col:
                i = col[tmp]
                ans[i].append(s)
            else:
                col[tmp] = idx
                ans.append([s])
                idx += 1
        return ans
        