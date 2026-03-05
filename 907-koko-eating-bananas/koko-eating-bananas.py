class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def get_hours(n):
            res = 0
            for i in piles:
                res+=math.ceil(i/n)
            return res

        while l<r:
            m = (l+r)//2

            if get_hours(m)<=h:
                r = m
            else:
                l = m+1
        return l
        