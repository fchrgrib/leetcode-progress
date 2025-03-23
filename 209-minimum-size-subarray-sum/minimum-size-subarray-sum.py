class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        d = sum_el = 0
        min_d = 2**31

        for i in range (len(nums)):
            if sum_el<target:
                sum_el+=nums[i]
                d+=1
            while sum_el>=target:
                min_d = min(min_d, d)
                sum_el-=nums[i-d+1]
                d-=1
                
        if min_d == 2**31:
            return 0
        return min_d

        