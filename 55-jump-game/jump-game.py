class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) ==1:
            return True
        sum_el = 0

        for i in range(len(nums)):
            if i == 0:
                sum_el = nums[i]
                continue
            if sum_el<i:
                return False
            sum_el = i+ max(sum_el - i, nums[i])
        return True
        