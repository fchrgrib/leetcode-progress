class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, l = 0, 0
        zero = 0
        ln = len(nums)

        for r in range(ln):
            if nums[r] == 0:
                zero+=1
            
            while zero>1:
                if nums[l] == 0:
                    zero-=1
                l+=1
            res = max(res, r-l)
        return res

        