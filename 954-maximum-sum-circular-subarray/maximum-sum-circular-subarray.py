class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        tmp = 0
        res = float("-inf")
        ln = len(nums)
        sum_back = 0

        max_back = [0 for i in range(len(nums))]
        for i in range(ln-1, 0, -1):
            if i == ln-1:
                max_back[i] = nums[i]
                sum_back = nums[i]
                continue
            sum_back+=nums[i]
            max_back[i] = max(max_back[i+1], sum_back)
        sum_back = 0
        for i in range(ln):
            tmp += nums[i]
            sum_back+=nums[i]
            res = max(res, nums[i])
            if tmp<0:
                tmp = 0
                continue
            res = max(res, tmp, nums[i], tmp if i == ln-1 else sum_back+max_back[i+1])
            

        return res
        