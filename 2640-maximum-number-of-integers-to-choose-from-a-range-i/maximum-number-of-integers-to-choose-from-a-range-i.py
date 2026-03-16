class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        sm = 0
        res = 0

        for num in range(1, n + 1):
            if num in banned:
                continue
            
            if sm + num > maxSum:
                break
            
            sm += num
            res += 1
        
        return res