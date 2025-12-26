class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        dp = {}

        if sm % 2 ==1:
            return False
        def dfs(idx, target):
            nonlocal nums
            if target == 0:
                return True
            if idx > len(nums)-1:
                return False
            if target <0:
                return False
            if (idx, target) in dp:
                return dp[(idx, target)]
            dp[(idx, target)] = dfs(idx+1, target-nums[idx]) or dfs(idx+1, target)
            
            return dp[(idx, target)]
        return dfs(0, sm//2)