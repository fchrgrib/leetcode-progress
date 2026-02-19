class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)

        if ls == 0 or lp == 0 or lp>ls:
            return []

        count_s, count_p, res = [0]*26, [0]*26, []

        for i in p:
            count_p[ord(i)-ord('a')]+=1
        for i in range(ls):
            if i-lp>=0:
                count_s[ord(s[i-lp])-ord('a')]-=1
            
            count_s[ord(s[i])-ord('a')]+=1
            
            if count_s == count_p:
                res.append(i-lp+1)
        return res
        