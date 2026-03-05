class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        prefix_sum = 1
        res = 0

        for r in range(len(nums)):
            prefix_sum*=nums[r]

            while l<r and prefix_sum>=k:
                prefix_sum//=nums[l]
                l+=1
            if prefix_sum<k:
                res+=(r-l+1)
        return res
        