class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        tmp = 26
        res = []
        while tmp>1:
            t = k-tmp
            if t>=0 and t>=n-1:
                res.append(chr(ord("a")+tmp-1))
                n-=1
                k=t
                continue
            if k<tmp:
                tmp = k
            else:
                tmp-=1
        if n > 0:
            res.append("a" * n)
        return "".join(res[::-1])
        