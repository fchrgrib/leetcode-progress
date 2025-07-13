class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if r ==0:
            if nums[r]<target:
                return 1
            else:
                return 0

        while l<r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m]<target:
                l = m+1
            else:
                r = m
        if l == r == len(nums) -1 and nums[r]<target:
            return len(nums)
        if l == r == len(nums) -1 and nums[r]>=target:
            return len(nums)-1
        
        if l == r:
            return l
        return -1
        