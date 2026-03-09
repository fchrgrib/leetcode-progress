class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        res = 0
        count_diff = 0


        for r in range(len(s)):
            count_diff += abs(ord(s[r]) - ord(t[r]))
            while count_diff>maxCost:
                count_diff-=(abs(ord(s[l]) - ord(t[l])))
                l+=1
            res = max(res, r-l+1)
        return res
        
        