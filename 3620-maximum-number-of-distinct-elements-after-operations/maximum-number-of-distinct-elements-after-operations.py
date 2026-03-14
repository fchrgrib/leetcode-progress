class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        min_s = -k
        res = 0
        nums.sort()

        if k == 0:
            return len(set(nums))

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                min_s+=1
            elif i>0 and nums[i] != nums[i-1]:
                min_s = min(min_s, max(nums[i-1] - nums[i] + min(min_s,k) + 1, -k))

            if min_s<=k:
                res+=1
        return res
        