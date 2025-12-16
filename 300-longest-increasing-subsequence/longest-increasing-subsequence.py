class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        icr_l = [1 for i in range(len(nums))]
        res = 1

        for i in range(1, len(nums)):
            for j in range(i,-1,-1):
                if nums[j]<nums[i]:
                    icr_l[i] = max(icr_l[j]+1, icr_l[i])
                    res = max(res, icr_l[i])
        return res
        