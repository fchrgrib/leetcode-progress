class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sum = 0
        global dp
        dp = {}

        n1 = len(text1)
        n2 = len(text2)
        def bc(t1, t2, idx1, idx2, n1, n2):
            global dp
            if idx1 == n1 or idx2 == n2:
                return 0
            if (idx1, idx2) in dp:
                return dp[(idx1, idx2)]
            
            dp[(idx1, idx2)] = 0
            if t1[idx1] == t2[idx2]:
                print(t1[idx1], t2[idx2])
                dp[(idx1, idx2)] = max(dp[(idx1, idx2)], 1 + bc(t1, t2, idx1+1, idx2+1, n1, n2))
            else:
                dp[(idx1, idx2)] = max(dp[(idx1, idx2)], bc(t1, t2, idx1+1, idx2, n1, n2))
                dp[(idx1, idx2)] = max(dp[(idx1, idx2)], bc(t1, t2, idx1+1, idx2+1, n1, n2))
                dp[(idx1, idx2)] = max(dp[(idx1, idx2)], bc(t1, t2, idx1, idx2+1, n1, n2))
            return dp[(idx1, idx2)]
        return bc(text1, text2, 0, 0, n1, n2)
        