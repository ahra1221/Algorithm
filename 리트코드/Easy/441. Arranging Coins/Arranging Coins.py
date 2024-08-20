class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 2
        while(n>1):
            if n - row >= 1 :
                n -= row
                row += 1
            else:
                break
        return row - 1
