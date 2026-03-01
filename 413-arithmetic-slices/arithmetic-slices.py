class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ln = len(nums)

        if ln<3:
            return 0
        
        l,res,prev = 0,0, float('inf')
        

        for i in range(1, ln):
            if prev != float("inf") and nums[i] - nums[i-1] != prev:
                l = i-1
                prev = nums[i] - nums[i-1]
            elif prev == float("inf"):
                prev = nums[i] - nums[i-1]
            
            if i-l>=2:
                res+=(i-l-1)
        return res

            