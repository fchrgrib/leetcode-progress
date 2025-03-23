class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        m = (l+r)//2

        while nums[m] > nums[r] or nums[m]<nums[l]:
            if nums[m] > nums[r]:
                l = m+1
            m = (l+r)//2
            if nums[m] < nums[l]:
                r = m
            # print(nums[l]," ",nums[r])
            m = (l+r)//2
        return nums[l]
