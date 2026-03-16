class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sm = 0
        stack = []
        banned = set(banned)
        ln = 0
        res = 0

        for num in range(1,n+1):
            if num in banned:
                continue
            sm+=num

            ln+=1
            stack.append(num)
            while sm>maxSum:
                sm -= stack.pop()
                ln-=1
            res = max(ln, res)
        return res
        