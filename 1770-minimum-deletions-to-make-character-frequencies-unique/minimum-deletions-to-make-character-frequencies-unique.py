class Solution:
    def minDeletions(self, s: str) -> int:
        dt = Counter(s)
        fq = set()
        dl = 0

        for key, val in dt.items():
            while val>0 and val in fq:
                val-=1
                dl+=1
            fq.add(val)
        return dl

        