class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        tmp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - tmp<0:
                return i-1
            tmp = nums[i]
        if len(nums)>1 and nums[len(nums)-1] - nums[len(nums)-2] >=1:
            return len(nums)-1
        return 0
        