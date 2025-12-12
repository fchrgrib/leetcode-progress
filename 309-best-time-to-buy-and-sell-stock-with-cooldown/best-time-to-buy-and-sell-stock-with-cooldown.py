class Solution:
    def maxProfit(self, p: List[int]) -> int:
        if len(p)<=1:
            return 0
        r, b, s, pr, pb, ps = 0, 0, 0, 0, -p[0], float("-inf")
        for i in range(1, len(p)):
            r = max(pr, ps)
            b = max(pr - p[i], pb)
            s = pb + p[i]
            pr = r
            pb = b
            ps = s
        
        return max(r,s)
                
        