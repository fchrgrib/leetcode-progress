class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)//2
            t1 = m-1
            t2 = m+1
            
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            if (nums[m]>nums[r] and nums[r]>target) or (nums[l]>nums[m] and nums[l]<target) :
                if nums[m]<target:
                    r = t1
                else:
                    l = t2
            else:
                if nums[m]<target:
                    l = t2
                else:
                    r = t1
        return -1

        