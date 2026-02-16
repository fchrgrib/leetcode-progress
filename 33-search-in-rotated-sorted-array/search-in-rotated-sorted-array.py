class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if r == 0:
            return r if nums[r] == target else -1

        while l<r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            if nums[l]<=nums[m]<target or nums[m]<target<=nums[r] or target<=nums[r]<nums[l]<=nums[m]:
                l = m+1
            else:
                r = m

        return l if nums[l] == target else -1

        