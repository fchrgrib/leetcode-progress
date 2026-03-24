class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        res = 0

        for num in nums:
            if num == 0:
                pos = neg = 0
            elif num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            else:
                pos, neg = (neg + 1 if neg > 0 else 0), pos + 1
            
            res = max(res, pos)
        
        return res