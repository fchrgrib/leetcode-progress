class Solution:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)

        if ln == 0:
            return 0
        if ln <= 2:
            return max(nums)

        
        res = float("-inf")
        for j in range(2):
            r, b, pr, pb = float("-inf"), 0, 0, nums[j]
            for i in range(1 if j ==0 else 2, ln-1 if j == 0 else ln):
                r = max(pr, pb)
                b = pr + nums[i]
                pb = b
                pr = r
                res = max(res, r, b)

        return res
        