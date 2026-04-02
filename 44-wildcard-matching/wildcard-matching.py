class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for j in range(m):
            if p[j] == "*":
                dp[0][j+1] = dp[0][j]
        
        for i in range(n):
            for j in range(m):
                if p[j] == s[i] or p[j] == "?":
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == "*":
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
        
        return dp[n][m]