class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ln1, ln2 = len(nums1), len(nums2)
        dp = [[0] * (ln2+1) for _ in range(ln1+1)]
        res = 0

        for i in range(1, ln1+1):
            for j in range(1, ln2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
        return res
        
        