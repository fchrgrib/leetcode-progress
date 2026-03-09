class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, l = 0, 0
        lb = [0,0]
        ln = len(nums)

        for r in range(ln):
            if nums[r] == 0:
                lb[0]+=1
            else:
                lb[1]+=1
            
            while lb[0]>1:
                if nums[l] == 0:
                    lb[0]-=1
                else:
                    lb[1]-=1
                l+=1
            if r-l+1 == lb[1]:
                res = max(res, lb[1]-1)
            else:
                res = max(res, lb[1])
        return res

        