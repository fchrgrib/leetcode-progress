class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n
        idx = n - 1
        while k > 0:
            val = min(k, 25)
            
            res[idx] = chr(ord('a') + val)
            k -= val
            idx -= 1
            
        return "".join(res)
        