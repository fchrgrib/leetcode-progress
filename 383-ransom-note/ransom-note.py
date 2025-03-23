class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        r_count = {}
        for i in r:
            r_count[i] = r.count(i)

        for k in r_count.keys():
            if r_count[k]>m.count(k):
                return False
        return True
        