class Solution:
    def numTrees(self, n: int) -> int:
        global dp
        dp = {}
        dp[0] = 1
        dp[1] = 1

        def catalan_number(n):
            global dp
            sum = 0
            for i in range(1,n+1):
                sum+=dp[i-1]*dp[n-i]
            return sum

        for i in range(2,n+1):
            dp[i] = catalan_number(i)
        return dp[n]
        