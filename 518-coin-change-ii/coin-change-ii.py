class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        for i in coins:
            for j in range(i, amount+1):
                tmp = j-i
                dp[j]+=dp[tmp]
        return dp[amount]
        