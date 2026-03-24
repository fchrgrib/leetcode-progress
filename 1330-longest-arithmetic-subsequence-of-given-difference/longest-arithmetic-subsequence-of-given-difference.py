class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = float("-inf")

        for num in arr:
            dp[num] = max(dp.get(num-difference,0)+1, dp.get(num,0))
            res = max(res, dp[num])
        return res
        