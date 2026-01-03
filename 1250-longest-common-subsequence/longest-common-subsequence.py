class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        lt1 = len(text1)
        lt2 = len(text2)

        def recurs(i, j):
            nonlocal text1, text2, lt1, lt2, dp
            if i>lt1-1 or j>lt2-1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if text1[i]==text2[j]:
                dp[i][j] = 1 + recurs(i+1, j+1)
            else:
                dp[i][j] = max({recurs(i+1,j), recurs(i,j+1)})
            return dp[i][j]
        
        return recurs(0,0)
        