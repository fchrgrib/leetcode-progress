class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        far_idx = {key: idx for idx, key in enumerate(s)}
        l, r = 0, 0
        res = []

        while r<len(s):
            res.append(1)
            ln = far_idx[s[l]]
            r = res[-1]
            while r<=ln:
                if s[r] in far_idx and far_idx[s[r]]>ln:
                    ln = far_idx[s[r]]
                r+=1
            res[-1] = r-l
            l = r
        return res
        