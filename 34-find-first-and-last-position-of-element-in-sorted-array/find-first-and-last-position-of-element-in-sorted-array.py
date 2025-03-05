class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        tmp = []

        l = 0
        r = len(nums)-1
        m = (l+r)//2

        while l<r:
            if nums[m] == target:
                break
            if nums[m]>target:
                r=m-1  
            else:
                l=m+1
            m= (l+r)//2
        if m<0 or nums[m] != target:
            return [-1,-1]
        
        i_min = i_max = m
        for i in range(i_max+1, len(nums)):
            if nums[i]!= target:
                break
            i_max = i
        for i in range(i_min-1, -1,-1):
            if nums[i]!= target:
                break
            i_min = i

        return [i_min, i_max]
        