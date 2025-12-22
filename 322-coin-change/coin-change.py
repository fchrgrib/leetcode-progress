class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        step = min(coins)
        
        for i in range(1,amount+1):
            for j in coins:
                tmp = i - j
                if tmp<0:
                    continue
                dp[i] = min(dp[i], dp[i-j] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1
            
        