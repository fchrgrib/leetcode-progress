class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ln = len(nums)
        dp = {}

        def recurs(i, target):
            nonlocal dp, ln, nums
            if i>ln:
                return 0
            if i == ln:
                return 1 if target==0 else 0
            if (i, target) in dp:
                return dp[(i, target)]
            
            dp[(i, target)] = recurs(i+1, target+nums[i]) + recurs(i+1, target-nums[i])
            return dp[(i, target)]

        return recurs(0, target)
        