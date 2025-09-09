class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = {}
        for n in nums:
            numdict[n] = numdict.get(n, 0) + 1
        return sorted(numdict, key=numdict.get, reverse=True)[:k]
