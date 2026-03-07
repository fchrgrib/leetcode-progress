class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res, l = 0, 0
        ln = len(prices)

        for i in range(ln):
            if i>0 and prices[i] - prices[i-1] != -1:
                l = i
            res+=(i-l+1)
        return res
        