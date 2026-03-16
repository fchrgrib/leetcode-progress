class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sm = 0
        stack = []
        banned = set(banned)
        res = 0

        for num in range(1,n+1):
            if num in banned:
                continue
            sm+=num
            stack.append(num)
            while sm>maxSum:
                sm -= stack.pop()
            res = max(len(stack), res)
        return res
        