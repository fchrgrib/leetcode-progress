class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l, ll = 0, 0
        g, g_l = 0, 0
        sg, sg_l = 0, 0
        ln = len(nums)

        for i in range(ln):
            if nums[i] == 1:
                sg+=1
                sg_l+=1
            
            while l<ln and sg>goal:
                if nums[l] == 1:
                    sg-=1
                l+=1
            
            while ll<ln and sg_l>goal-1:
                if nums[ll] == 1:
                    sg_l-=1
                ll+=1
            
            g += (i-l+1)
            g_l += (i-ll+1)
        return g-g_l if goal>0 else g
        